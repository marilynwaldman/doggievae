from sklearn import preprocessing

'''

Taken from Abhishek Thakur's book and github, this module converts categorical data into ohe or 
labeled data.  Documentation here:

https://www.youtube.com/watch?v=vkXEHpuu03A&list=PL98nY_tJQXZnKfgWIADbBG182nFUNIsxw&index=4

and github here:

https://github.com/abhi1thakur/mlframework


'''


class CategoricalFeatures:
    def __init__(self, df, categorical_features, encoding_type, handle_na=False):
        """
        df: pandas dataframe
        categorical_features: list of column names, e.g. ["ord_1", "nom_0"......]
        encoding_type: label, binary, ohe
        handle_na: True/False
        """
        self.df = df
        self.cat_feats = categorical_features
        self.enc_type = encoding_type
        self.handle_na = handle_na
        self.label_encoders = dict()
        self.binary_encoders = dict()
        self.ohe = None

        if self.handle_na:
            for c in self.cat_feats:
                self.df.loc[:, c] = self.df.loc[:, c].astype(str).fillna("-9999999") #!!NA
        self.output_df = self.df.copy(deep=True)
    
    def _label_encoding(self):
        for c in self.cat_feats:
            lbl = preprocessing.LabelEncoder()
            lbl.fit(self.df[c].values)
            self.output_df.loc[:, c] = lbl.transform(self.df[c].values)
            self.label_encoders[c] = lbl
        return self.output_df
    

    def _one_hot(self):
        ohe = preprocessing.OneHotEncoder(sparse=False)
        ohe.fit(self.df[self.cat_feats].values)
        return ohe.transform(self.df[self.cat_feats].values)

    def fit_transform(self):
        if self.enc_type == "label":
            return self._label_encoding()
        elif self.enc_type == "ohe":
            return self._one_hot()
        else:
            raise Exception("Encoding type not understood")
    
    def transform(self, dataframe):
        if self.handle_na:
            for c in self.cat_feats:
                dataframe.loc[:, c] = dataframe.loc[:, c].astype(str).fillna("-9999999")

        if self.enc_type == "label":
            for c, lbl in self.label_encoders.items():
                dataframe.loc[:, c] = lbl.transform(dataframe[c].values)
            return dataframe

        elif self.enc_type == "ohe":
            return self.ohe(dataframe[self.cat_feats].values)
        
        else:
            raise Exception("Encoding type not understood")
                

if __name__ == "__main__":
    import pandas as pd
    from sklearn import linear_model
    df = pd.read_csv("./data/ex4_2.csv")
    #df_test = pd.read_csv("../input/test_cat.csv")
    #sample = pd.read_csv("../input/sample_submission.csv")


    train_len = len(df)
    
    #fake a target value for dataset completeness
    df["target"] = -1
    
    full_data = df

    cols = [c for c in df.columns if c not in ["target"]]
    print(cols)
    cat_feats = CategoricalFeatures(full_data, 
                                    categorical_features=cols, 
                                    encoding_type="ohe",
                                    handle_na=True)   ### note handle NAN !!!
    full_data_transformed = cat_feats.fit_transform()

    print(type(full_data_transformed))
    print(full_data_transformed.shape)

    df1 = pd.DataFrame(full_data_transformed)
    print(df1.head())
    
    #X = full_data_transformed[:train_len, :]
    #X_test = full_data_transformed[train_len:, :]

    #clf = linear_model.LogisticRegression()
    #clf.fit(X, df.target.values)
    #preds = clf.predict_proba(X_test)[:, 1]
    
    #sample.loc[:, "target"] = preds
    #sample.to_csv("submission.csv", index=False)
