class MLServiceImpl:
    def ping(self):
        print('ping()')

    def buildModel(self, dataSetId, modelType):
        print 'building model %s for %s' % (dataSetId, modelType)

    def predict(self, modelId, dataInput):
        print 'predicting %s using model %s' % (dataInput, modelId)
        return {1: 1.0}
