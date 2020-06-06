from sklearn.model_selection import RandomizedSearchCV,train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error,mean_absolute_error
from data import *

X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed = train_test_split(days_since_1_22, world_cases, test_size=0.15, shuffle=False)





kernel = ['poly','sigmoid','rbf']
c = [0.01,0.1,1,10]
gamma = [0.01,0.1,1]
epsilon = [0.01,0.1,1]
shrinking = [True,False]
svm_grid = {'kernel':kernel,'C': c,'gamma':gamma,'epsilon':epsilon,'shrinking':shrinking}
svm=SVR()
svm_search= RandomizedSearchCV(svm,svm_grid,scoring='neg_mean_squared_error',cv=3,return_train_score = True,n_jobs=-1,n_iter=40,verbose=1)
svm_search.fit(X_train_confirmed,y_train_confirmed)










svm_confirmed = svm_search.best_estimator_





svm_pred = svm_confirmed.predict(future_forecast)















svm_test_pred = svm_confirmed.predict(X_test_confirmed)
plt.plot(svm_test_pred,label='Predicted')
plt.plot(y_test_confirmed,label='Actual')
plt.legend()
plt.show()





print('absolute error :',mean_absolute_error(svm_test_pred,y_test_confirmed))
print('squared error :',mean_squared_error(svm_test_pred,y_test_confirmed))





plt.figure(figsize=(20,12))
plt.plot(adjusted_dates,world_cases)
plt.xlabel('Days since 22/1/20',size=30)
plt.ylabel('cases',size=30)
plt.xticks(np.arange(0,110,10),size=15)
plt.yticks(size=15)





plt.figure(figsize=(20,12))
plt.plot(adjusted_dates,world_cases)
plt.plot(future_forecast,svm_pred,linestyle='dashed',color='purple')
plt.xlabel('Days since 22/1/20',size=30)
plt.ylabel('cases',size=30)
plt.legend(['confirmed cases','predicted cases'])
plt.xticks(size=15)
plt.yticks(size=15)
plt.show()



