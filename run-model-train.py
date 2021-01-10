from model import model_train, model_load
import os

def main(data_dir):
    
    ## train the model
    model_train(data_dir, test=False)

    ## load the model
    model = model_load()
    
    print("model training complete.")


if __name__ == "__main__":

    data_dir = os.path.join(os.getcwd(),"data","cs-train")
    main(data_dir)
