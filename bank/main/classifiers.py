import joblib

def risk_calc(model, inp):
    fact = model.predict_proba([inp])
    return fact[:, 1]

def classifier(inp):
    # sequence = ['accuracy", "recall", "f1-score", "precision", "roc_auc_score"]
    lgr_metrics = [84.13 , 45.74 , 56.05 , 72.35 , 85.46 ]
    knn_metrics = [85.22 , 40.19 , 54.60 , 85.11 , 87.65 ]
    dt_metrics = [92.25 , 70.81 , 80.16 , 92.34 , 90.80 ]
    nb_metrics = [81.81 , 64.15 , 60.94 , 58.03 , 84.60 ]
    # xgb_metrics = [93.38 , 72.94 , 82.98 , 96.22 , 94.73 ]
    mlp_metrics = [91.23 , 68.96 , 77.68 , 88.91 , 91.11 ]

    inp_final = inp
    risk_fact = []
    # preds_proba = model.predict_proba(x_test)
    # clf_ = joblib.load("mlp.pkl")
#   print(f"Result : {clf_.predict(inp)}")
    lgr_clf = joblib.load("pkl/lgr.pkl")
    lgr_res = lgr_clf.predict([inp_final])
    # fact = lgr_clf.predict_proba([inp_final])
    risk_fact.append(risk_calc(lgr_clf, inp_final))
#   print(f"Result : {clf_.predict(inp)}")
    knn_clf = joblib.load("pkl/knn.pkl")
    knn_res = knn_clf.predict([inp_final])
    risk_fact.append(risk_calc(knn_clf, inp_final))
#   print(f"Result : {clf_.predict(inp)}")
    dt_clf = joblib.load("pkl/dt.pkl")
    dt_res = dt_clf.predict([inp_final])
    risk_fact.append(risk_calc(dt_clf, inp_final))
#   print(f"Result : {clf_.predict(inp)}")
    nb_clf = joblib.load("pkl/nb.pkl")
    nb_res = nb_clf.predict([inp_final])
    risk_fact.append(risk_calc(nb_clf, inp_final))
#   print(f"Result : {clf_.predict(inp)}")
    mlp_clf = joblib.load("pkl/mlp.pkl")
    mlp_res = mlp_clf.predict([inp_final])
    risk_fact.append(risk_calc(mlp_clf, inp_final))

    lgr_metrics.append(lgr_res[0])
    knn_metrics.append(knn_res[0])
    nb_metrics.append(nb_res[0])
    dt_metrics.append(dt_res[0])
    mlp_metrics.append(mlp_res[0])

    res_final = {"lgr" : lgr_metrics,
                 "knn" : knn_metrics,
                 "dt" : dt_metrics,
                 "nb" : nb_metrics,
                 "mlp" : mlp_metrics}
    # print(f"Result : {res_final}")
    # print(f"Risk Factor : {risk_fact}")
    res_final["risk_factors"] = risk_fact

    return res_final
    
# b = [21, 9600, 5.0, 20.90, 1000, 11.14, 0.10, 1, 2]

# classifier(b)