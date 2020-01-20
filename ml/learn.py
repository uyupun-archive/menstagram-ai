# VGG16 + 転移学習で学習する

from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D, Input
from keras.optimizers import SGD
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator

IMAGE_SIZE = 224
CATEGORIES = 3
BATCH_SIZE = 16
EPOCHS = 50
TRAINING = 1600
VALIDATION = 400

input_tensor = Input(shape = (IMAGE_SIZE, IMAGE_SIZE, 3))
base_model = VGG16(weights = 'imagenet', include_top = False, input_tensor = input_tensor)

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation = 'relu')(x)
outputs = Dense(CATEGORIES, activation = 'softmax')(x)
model = Model(inputs = base_model.input, outputs = outputs)

for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer = SGD(lr = 0.0001, momentum = 0.9), loss = 'cross_crossentropy', metrics = ['accuracy'])

model.summary()

train_data_dir = './learn_data/train'
validation_data_dir = './learn_data/validation'

train_data_gen = ImageDataGenerator(
    rescale = 1.0 / 255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    rotation_range = 10)
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

history = model.fit_generator(train_generator,
   steps_per_epoch = TRAINING // BATCH_SIZE,
   epochs = EPOCHS,
   verbose = 1,
   validation_data = validation_generator,
   validation_steps = VALIDATION // BATCH_SIZE,
)

model.save('judge-ramen-model.h5')