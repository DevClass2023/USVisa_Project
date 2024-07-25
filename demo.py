from us_visa.pipline.training_pipeline import TrainPipeline
import os
os.environ['LOKY_MAX_CPU_COUNT'] = '4'  # Adjust to your number of cores


obj = TrainPipeline()
obj.run_pipeline()