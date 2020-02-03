# VGG16 + 転移学習で学習する

from keras.models import Sequential, Model
from keras.layers import Input, Flatten, Dense, Dropout
from keras.optimizers import SGD
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator

IMAGE_SIZE = 224
CLASSES = ['ramen', 'other']
CLASSES_LEN = len(CLASSES)
BATCH_SIZE = 5
EPOCHS = 50
TRAININGS = 30
VALIDATIONS = 5

train_data_dir = 'trainer/learn_data/train'
validation_data_dir = 'trainer/learn_data/validation'

input_tensor = Input(shape = (IMAGE_SIZE, IMAGE_SIZE, 3))
base_model = VGG16(weights = 'imagenet', include_top = False, input_tensor = input_tensor)

model = Sequential()
model.add(Flatten(input_shape = base_model.output_shape[1:]))
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(CLASSES_LEN, activation = 'softmax'))

model = Model(input = base_model.input, output = model(base_model.output))

for layer in model.layers[:15]:
    layer.trainable = False

model.compile(optimizer = SGD(lr = 1e-3, momentum = 0.9), loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.summary()

train_data_gen = ImageDataGenerator(
    rescale = 1.0 / 255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    rotation_range = 10
)
validation_data_gen = ImageDataGenerator(
    rescale = 1.0 / 255,
)

train_generator = train_data_gen.flow_from_directory(
    train_data_dir,
    target_size = (IMAGE_SIZE, IMAGE_SIZE),
    batch_size = BATCH_SIZE,
    class_mode = 'categorical',
    shuffle = True
)
validation_generator = validation_data_gen.flow_from_directory(
    validation_data_dir,
    target_size = (IMAGE_SIZE, IMAGE_SIZE),
    batch_size = BATCH_SIZE,
    class_mode = 'categorical',
    shuffle = True
)

history = model.fit_generator(
    train_generator,
    steps_per_epoch = TRAININGS // BATCH_SIZE,
    epochs = EPOCHS,
    verbose = 1,
    validation_data = validation_generator,
    validation_steps = VALIDATIONS // BATCH_SIZE,
)

model.save('trainer/judge-ramen-model.h5')