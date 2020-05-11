import os

# python src/main.py --train-graph-folder ./GAM_Input/Train/ --test-graph-folder ./GAM_Input/Test/ --epochs 50


DEFAULT_NAME = 'Experiment_'
DEFAULT_TEST = '--test-graph-folder ./GAM_Input/Test/ '
DEFAULT_TRAIN = '--train-graph-folder ./GAM_Input/Train/ '
DEFAULT_OUTPUT = '--prediction-path ./Experiment_outputs/'
DEFAULT_LOG = '--log-path  ./Experiment_logs/'
OFFSET = 0

EXPERIMENTS = [
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 10,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 100,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 200,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 300,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 400,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 500,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 1000,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 10,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 1500,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },
    {
        'repetitions': 10,
        'batch-size': 32,
        'time': 20,
        'step-dimensions': 32,
        'combined-dimensions': 64,
        'epochs': 2000,
        'learning-rate': 0.001,
        'gamma': 0.99,
        'weight-decay': 0.00001,    
    },

]

CMD = "python src/main.py "
# CMD = "echo python src/main.py "

for i in range(0, len(EXPERIMENTS)):
    experiment_number = i+OFFSET
    command = CMD \
        + DEFAULT_TRAIN  \
        + DEFAULT_TEST  \
        + DEFAULT_OUTPUT + DEFAULT_NAME + str(experiment_number) + '.csv ' \
        + DEFAULT_LOG + DEFAULT_NAME + str(experiment_number) + '.json '  \
        + '--repetitions ' + str(EXPERIMENTS[i]['repetitions']) + ' ' \
        + '--batch-size ' + str(EXPERIMENTS[i]['batch-size']) + ' ' \
        + '--time ' + str(EXPERIMENTS[i]['time']) + ' ' \
        + '--step-dimensions ' + str(EXPERIMENTS[i]['step-dimensions']) + ' ' \
        + '--combined-dimensions ' + str(EXPERIMENTS[i]['combined-dimensions']) + ' ' \
        + '--epochs ' + str(EXPERIMENTS[i]['epochs']) + ' ' \
        + '--learning-rate ' + str(EXPERIMENTS[i]['learning-rate']) + ' ' \
        + '--gamma ' + str(EXPERIMENTS[i]['gamma']) + ' ' \
        + '--weight-decay ' + str(EXPERIMENTS[i]['weight-decay']) + ' ' 

    
    os.system(command)