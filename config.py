#################
# Misc settings #
#################

# Random seed for gaussian noise
RANDOM_SEED: int = 42

##########################
# Model paths and config #
##########################

MODEL_VESION: str = 'V2.4'
PB_MODEL: str = 'checkpoints/V2.4/BirdNET_GLOBAL_6K_V2.4_Model'
# MODEL_PATH = PB_MODEL # This will load the protobuf model
MODEL_PATH: str = 'checkpoints/V2.4/BirdNET_GLOBAL_6K_V2.4_Model_FP32.tflite'
MDATA_MODEL_PATH: str = 'checkpoints/V2.4/BirdNET_GLOBAL_6K_V2.4_MData_Model_FP16.tflite'
LABELS_FILE: str = 'checkpoints/V2.4/BirdNET_GLOBAL_6K_V2.4_Labels.txt'
TRANSLATED_LABELS_PATH:str = 'labels/V2.4'

# Path to custom trained classifier
# If None, no custom classifier will be used
# Make sure to set the LABELS_FILE above accordingly
CUSTOM_CLASSIFIER = None

##################
# Audio settings #
##################

# We use a sample rate of 48kHz, so the model input size is 
# (batch size, 48000 kHz * 3 seconds) = (1, 144000)
# Recordings will be resampled automatically.
SAMPLE_RATE: int = 48000 

# We're using 3-second chunks
SIG_LENGTH: float = 3.0 

# Define overlap between consecutive chunks <3.0; 0 = no overlap
SIG_OVERLAP: float = 0 

# Define minimum length of audio chunk for prediction, 
# chunks shorter than 3 seconds will be padded with zeros
SIG_MINLEN: float = 1.0 

# Frequency range. This is model specific and should not be changed.
SIG_FMIN: int = 0
SIG_FMAX: int = 15000

#####################
# Metadata settings #
#####################

LATITUDE: float = -1
LONGITUDE:float = -1
WEEK: int = -1
LOCATION_FILTER_THRESHOLD: float = 0.03

######################
# Inference settings #
######################

# If None or empty file, no custom species list will be used
# Note: Entries in this list have to match entries from the LABELS_FILE
# We use the 2021 eBird taxonomy for species names (Clements list)
CODES_FILE: str = 'eBird_taxonomy_codes_2021E.json'
SPECIES_LIST_FILE: str = 'example/species_list.txt' 

# File input path and output path for selection tables
INPUT_PATH: str = 'example/'
OUTPUT_PATH: str = 'example/'

# Supported file types
ALLOWED_FILETYPES: list[str] = ['wav', 'flac', 'mp3', 'ogg', 'm4a', 'wma', 'aiff', 'aif']

# Number of threads to use for inference.
# Can be as high as number of CPUs in your system
CPU_THREADS: int = 8
TFLITE_THREADS: int = 1 

# False will output logits, True will convert to sigmoid activations
APPLY_SIGMOID: bool = True 
SIGMOID_SENSITIVITY: float = 1.0

# Minimum confidence score to include in selection table 
# (be aware: if APPLY_SIGMOID = False, this no longer represents 
# probabilities and needs to be adjusted)
MIN_CONFIDENCE: float = 0.1 

# Number of samples to process at the same time. Higher values can increase
# processing speed, but will also increase memory usage.
# Might only be useful for GPU inference.
BATCH_SIZE: int = 1

# Specifies the output format. 'table' denotes a Raven selection table,
# 'audacity' denotes a TXT file with the same format as Audacity timeline labels
# 'csv' denotes a generic CSV file with start, end, species and confidence.
RESULT_TYPE: str = 'table'

#####################
# Training settings #
#####################

# Training data path
TRAIN_DATA_PATH: str = 'train_data/'

# Sample crop mode
SAMPLE_CROP_MODE: str = 'center'

# List of non-event classes
NON_EVENT_CLASSES: list[str] = ["noise", "other", "background", "silence"]

# Upsampling settings
UPSAMPLING_RATIO: float = 0.0
UPSAMPLING_MODE = 'repeat'

# Number of epochs to train for
TRAIN_EPOCHS: int = 100

# Batch size for training
TRAIN_BATCH_SIZE: int = 32

# Validation split (percentage)
TRAIN_VAL_SPLIT: float = 0.2

# Learning rate for training
TRAIN_LEARNING_RATE: float = 0.01

# Number of hidden units in custom classifier
# If >0, a two-layer classifier will be trained
TRAIN_HIDDEN_UNITS: int = 0

# Dropout rate for training
TRAIN_DROPOUT: float = 0.0

# Whether to use mixup for training
TRAIN_WITH_MIXUP: bool = False

# Whether to apply label smoothing for training
TRAIN_WITH_LABEL_SMOOTHING: bool = False

# Model output format
TRAINED_MODEL_OUTPUT_FORMAT: str = 'tflite'

# Cache settings
TRAIN_CACHE_MODE: str = 'none'
TRAIN_CACHE_FILE: str = 'train_cache.npz'

#####################
# Misc runtime vars #
#####################
CODES = {}
LABELS: list[str] = []
TRANSLATED_LABELS: list[str] = []
SPECIES_LIST: list[str] = []
ERROR_LOG_FILE: str = 'error_log.txt'
FILE_LIST = []
FILE_STORAGE_PATH: str = ''

######################
# Get and set config #
######################

def getConfig():
    return {
        'RANDOM_SEED': RANDOM_SEED,
        'MODEL_VESION': MODEL_VESION,
        'PB_MODEL': PB_MODEL,
        'MODEL_PATH': MODEL_PATH,
        'MDATA_MODEL_PATH': MDATA_MODEL_PATH,
        'LABELS_FILE': LABELS_FILE,
        'TRANSLATED_LABELS_PATH': TRANSLATED_LABELS_PATH,
        'CUSTOM_CLASSIFIER': CUSTOM_CLASSIFIER,
        'SAMPLE_RATE': SAMPLE_RATE,
        'SIG_LENGTH': SIG_LENGTH,
        'SIG_OVERLAP': SIG_OVERLAP,
        'SIG_MINLEN': SIG_MINLEN,
        'SIG_FMIN': SIG_FMIN,
        'SIG_FMAX': SIG_FMAX,
        'LATITUDE': LATITUDE,
        'LONGITUDE': LONGITUDE,
        'WEEK': WEEK,
        'LOCATION_FILTER_THRESHOLD': LOCATION_FILTER_THRESHOLD,
        'CODES_FILE': CODES_FILE,
        'SPECIES_LIST_FILE': SPECIES_LIST_FILE,
        'ALLOWED_FILETYPES': ALLOWED_FILETYPES,
        'INPUT_PATH': INPUT_PATH,
        'OUTPUT_PATH': OUTPUT_PATH,
        'CPU_THREADS': CPU_THREADS,
        'TFLITE_THREADS': TFLITE_THREADS,
        'APPLY_SIGMOID': APPLY_SIGMOID,
        'SIGMOID_SENSITIVITY': SIGMOID_SENSITIVITY,
        'MIN_CONFIDENCE': MIN_CONFIDENCE,
        'BATCH_SIZE': BATCH_SIZE,
        'RESULT_TYPE': RESULT_TYPE,
        'TRAIN_DATA_PATH': TRAIN_DATA_PATH,
        'SAMPLE_CROP_MODE': SAMPLE_CROP_MODE,
        'NON_EVENT_CLASSES': NON_EVENT_CLASSES,
        'UPSAMPLING_RATIO': UPSAMPLING_RATIO,
        'UPSAMPLING_MODE': UPSAMPLING_MODE,
        'TRAIN_EPOCHS': TRAIN_EPOCHS,
        'TRAIN_VAL_SPLIT': TRAIN_VAL_SPLIT,
        'TRAIN_BATCH_SIZE': TRAIN_BATCH_SIZE,
        'TRAIN_LEARNING_RATE': TRAIN_LEARNING_RATE,
        'TRAIN_HIDDEN_UNITS': TRAIN_HIDDEN_UNITS,
        'TRAIN_DROPOUT': TRAIN_DROPOUT,
        'TRAIN_WITH_MIXUP': TRAIN_WITH_MIXUP,
        'TRAIN_WITH_LABEL_SMOOTHING': TRAIN_WITH_LABEL_SMOOTHING,
        'TRAINED_MODEL_OUTPUT_FORMAT': TRAINED_MODEL_OUTPUT_FORMAT,
        'TRAIN_CACHE_MODE': TRAIN_CACHE_MODE,
        'TRAIN_CACHE_FILE': TRAIN_CACHE_FILE,
        'CODES': CODES,
        'LABELS': LABELS,
        'TRANSLATED_LABELS': TRANSLATED_LABELS,
        'SPECIES_LIST': SPECIES_LIST,
        'ERROR_LOG_FILE': ERROR_LOG_FILE,
        'FILE_LIST': FILE_LIST,
        'FILE_STORAGE_PATH': FILE_STORAGE_PATH
    }

def setConfig(c):

    global RANDOM_SEED
    global MODEL_VESION
    global PB_MODEL
    global MODEL_PATH
    global MDATA_MODEL_PATH
    global LABELS_FILE
    global TRANSLATED_LABELS_PATH
    global CUSTOM_CLASSIFIER
    global SAMPLE_RATE
    global SIG_LENGTH
    global SIG_OVERLAP
    global SIG_MINLEN
    global SIG_FMIN
    global SIG_FMAX
    global LATITUDE
    global LONGITUDE
    global WEEK
    global LOCATION_FILTER_THRESHOLD
    global CODES_FILE
    global SPECIES_LIST_FILE
    global ALLOWED_FILETYPES
    global INPUT_PATH
    global OUTPUT_PATH
    global CPU_THREADS
    global TFLITE_THREADS
    global APPLY_SIGMOID
    global SIGMOID_SENSITIVITY
    global MIN_CONFIDENCE
    global BATCH_SIZE
    global RESULT_TYPE
    global TRAIN_DATA_PATH
    global SAMPLE_CROP_MODE
    global NON_EVENT_CLASSES
    global UPSAMPLING_RATIO
    global UPSAMPLING_MODE
    global TRAIN_EPOCHS
    global TRAIN_VAL_SPLIT
    global TRAIN_BATCH_SIZE
    global TRAIN_LEARNING_RATE
    global TRAIN_HIDDEN_UNITS
    global TRAIN_DROPOUT
    global TRAIN_WITH_MIXUP
    global TRAIN_WITH_LABEL_SMOOTHING
    global TRAINED_MODEL_OUTPUT_FORMAT
    global TRAIN_CACHE_MODE
    global TRAIN_CACHE_FILE
    global CODES
    global LABELS
    global TRANSLATED_LABELS
    global SPECIES_LIST
    global ERROR_LOG_FILE
    global FILE_LIST
    global FILE_STORAGE_PATH

    RANDOM_SEED = c['RANDOM_SEED']
    MODEL_VESION = c['MODEL_VESION']
    PB_MODEL = c['PB_MODEL']
    MODEL_PATH = c['MODEL_PATH']
    MDATA_MODEL_PATH = c['MDATA_MODEL_PATH']
    LABELS_FILE = c['LABELS_FILE']
    TRANSLATED_LABELS_PATH = c['TRANSLATED_LABELS_PATH']
    CUSTOM_CLASSIFIER = c['CUSTOM_CLASSIFIER']
    SAMPLE_RATE = c['SAMPLE_RATE']
    SIG_LENGTH = c['SIG_LENGTH']
    SIG_OVERLAP = c['SIG_OVERLAP']
    SIG_MINLEN = c['SIG_MINLEN']
    SIG_FMIN = c['SIG_FMIN']
    SIG_FMAX = c['SIG_FMAX']
    LATITUDE = c['LATITUDE']
    LONGITUDE = c['LONGITUDE']
    WEEK = c['WEEK']
    LOCATION_FILTER_THRESHOLD = c['LOCATION_FILTER_THRESHOLD']
    CODES_FILE = c['CODES_FILE']
    SPECIES_LIST_FILE = c['SPECIES_LIST_FILE']
    ALLOWED_FILETYPES = c['ALLOWED_FILETYPES']
    INPUT_PATH = c['INPUT_PATH']
    OUTPUT_PATH = c['OUTPUT_PATH']
    CPU_THREADS = c['CPU_THREADS']
    TFLITE_THREADS = c['TFLITE_THREADS']
    APPLY_SIGMOID = c['APPLY_SIGMOID']
    SIGMOID_SENSITIVITY = c['SIGMOID_SENSITIVITY']
    MIN_CONFIDENCE = c['MIN_CONFIDENCE']
    BATCH_SIZE = c['BATCH_SIZE']
    RESULT_TYPE = c['RESULT_TYPE']
    TRAIN_DATA_PATH = c['TRAIN_DATA_PATH']
    SAMPLE_CROP_MODE = c['SAMPLE_CROP_MODE']
    NON_EVENT_CLASSES = c['NON_EVENT_CLASSES']
    UPSAMPLING_RATIO = c['UPSAMPLING_RATIO']
    UPSAMPLING_MODE = c['UPSAMPLING_MODE']
    TRAIN_EPOCHS = c['TRAIN_EPOCHS']
    TRAIN_VAL_SPLIT = c['TRAIN_VAL_SPLIT']
    TRAIN_BATCH_SIZE = c['TRAIN_BATCH_SIZE']
    TRAIN_LEARNING_RATE = c['TRAIN_LEARNING_RATE']
    TRAIN_HIDDEN_UNITS = c['TRAIN_HIDDEN_UNITS']
    TRAIN_DROPOUT = c['TRAIN_DROPOUT']
    TRAIN_WITH_MIXUP = c['TRAIN_WITH_MIXUP']
    TRAIN_WITH_LABEL_SMOOTHING = c['TRAIN_WITH_LABEL_SMOOTHING']
    TRAINED_MODEL_OUTPUT_FORMAT = c['TRAINED_MODEL_OUTPUT_FORMAT']
    TRAIN_CACHE_MODE = c['TRAIN_CACHE_MODE']
    TRAIN_CACHE_FILE = c['TRAIN_CACHE_FILE']
    CODES = c['CODES']
    LABELS = c['LABELS']
    TRANSLATED_LABELS = c['TRANSLATED_LABELS']
    SPECIES_LIST = c['SPECIES_LIST']
    ERROR_LOG_FILE = c['ERROR_LOG_FILE']
    FILE_LIST = c['FILE_LIST']
    FILE_STORAGE_PATH = c['FILE_STORAGE_PATH']
