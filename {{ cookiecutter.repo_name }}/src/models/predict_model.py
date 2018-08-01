import os
import pickle
import pandas as pd
from sklearn.metrics import roc_auc_score
from train_model import ROOT


def retrieve_model():
    """retrieve the pickled model object
    """
    pickled_model = os.path.join(ROOT, 'models/transfusion.model')
    with open(pickled_model, 'rb') as fin:
        return(pickle.load(fin))
    

def main():
    """ retrieve the model and predict labels. Show prediction and performance
    """
    deserialized_model = retrieve_model()
    X_test = pd.read_csv(os.path.join(ROOT, 
        'data/processed/transfusion_x_test.csv'))
    y_pred = deserialized_model.predict(X_test)

    y_test = pd.read_csv(os.path.join(ROOT,
        'data/processed/transfusion_y_test.csv'), header=None)
    print(f'The model returned these predictions:\n{y_pred}')

    auc = roc_auc_score(y_test.astype(int), deserialized_model.predict_proba(X_test)[:, 1])
    print('AUC (area under ROC curve): ' + str(auc))

if __name__ == '__main__':
    main()
