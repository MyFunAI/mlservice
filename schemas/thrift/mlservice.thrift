typedef map<i32, double> Vector;

struct DataSet {
  1: string id,
}

enum ModelType {
}

struct Model {
  1: string id,
  2: string dataSetId,
  3: ModelType type,
}

service MLService {
  void ping(),
  void buildModel(1:string dataSetId, 2:ModelType modelType),
  Vector predict(1:string modelId, 2:Vector input),
}
