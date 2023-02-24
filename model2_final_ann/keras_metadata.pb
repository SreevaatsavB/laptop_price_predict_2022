
�Qroot"_tf_keras_network*�Q{"name": "model_11", "trainable": true, "expects_training_arg": true, "dtype": "float32", "batch_input_shape": null, "must_restore_from_config": false, "class_name": "Functional", "config": {"name": "model_11", "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 17]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "input_23"}, "name": "input_23", "inbound_nodes": []}, {"class_name": "Dense", "config": {"name": "dense_99", "trainable": true, "dtype": "float32", "units": 32, "activation": {"class_name": "LeakyReLU", "config": {"name": "leaky_re_lu_22", "trainable": true, "dtype": "float32", "alpha": 0.0024999999441206455}}, "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "name": "dense_99", "inbound_nodes": [[["input_23", 0, 0, {}]]]}, {"class_name": "Dense", "config": {"name": "dense_100", "trainable": true, "dtype": "float32", "units": 25, "activation": {"class_name": "LeakyReLU", "config": {"name": "leaky_re_lu_23", "trainable": true, "dtype": "float32", "alpha": 0.001500000013038516}}, "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "name": "dense_100", "inbound_nodes": [[["input_23", 0, 0, {}]]]}, {"class_name": "BatchNormalization", "config": {"name": "batch_normalization_22", "trainable": true, "dtype": "float32", "axis": [1], "momentum": 0.99, "epsilon": 0.001, "center": true, "scale": true, "beta_initializer": {"class_name": "Zeros", "config": {}}, "gamma_initializer": {"class_name": "Ones", "config": {}}, "moving_mean_initializer": {"class_name": "Zeros", "config": {}}, "moving_variance_initializer": {"class_name": "Ones", "config": {}}, "beta_regularizer": null, "gamma_regularizer": null, "beta_constraint": null, "gamma_constraint": null}, "name": "batch_normalization_22", "inbound_nodes": [[["dense_99", 0, 0, {}]]]}, {"class_name": "BatchNormalization", "config": {"name": "batch_normalization_23", "trainable": true, "dtype": "float32", "axis": [1], "momentum": 0.99, "epsilon": 0.001, "center": true, "scale": true, "beta_initializer": {"class_name": "Zeros", "config": {}}, "gamma_initializer": {"class_name": "Ones", "config": {}}, "moving_mean_initializer": {"class_name": "Zeros", "config": {}}, "moving_variance_initializer": {"class_name": "Ones", "config": {}}, "beta_regularizer": null, "gamma_regularizer": null, "beta_constraint": null, "gamma_constraint": null}, "name": "batch_normalization_23", "inbound_nodes": [[["dense_100", 0, 0, {}]]]}, {"class_name": "Concatenate", "config": {"name": "concatenate_11", "trainable": true, "dtype": "float32", "axis": -1}, "name": "concatenate_11", "inbound_nodes": [[["batch_normalization_22", 0, 0, {}], ["batch_normalization_23", 0, 0, {}]]]}, {"class_name": "Dense", "config": {"name": "dense_101", "trainable": true, "dtype": "float32", "units": 20, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": {"class_name": "L2", "config": {"l2": 0.009999999776482582}}, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "name": "dense_101", "inbound_nodes": [[["concatenate_11", 0, 0, {}]]]}, {"class_name": "Dense", "config": {"name": "dense_102", "trainable": true, "dtype": "float32", "units": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "name": "dense_102", "inbound_nodes": [[["dense_101", 0, 0, {}]]]}], "input_layers": [["input_23", 0, 0]], "output_layers": [["dense_102", 0, 0]]}, "shared_object_id": 27, "input_spec": [{"class_name": "InputSpec", "config": {"dtype": null, "shape": {"class_name": "__tuple__", "items": [null, 17]}, "ndim": 2, "max_ndim": null, "min_ndim": null, "axes": {}}}], "build_input_shape": {"class_name": "TensorShape", "items": [null, 17]}, "is_graph_network": true, "full_save_spec": {"class_name": "__tuple__", "items": [[{"class_name": "TypeSpec", "type_spec": "tf.TensorSpec", "serialized": [{"class_name": "TensorShape", "items": [null, 17]}, "float32", "input_23"]}], {}]}, "save_spec": {"class_name": "TypeSpec", "type_spec": "tf.TensorSpec", "serialized": [{"class_name": "TensorShape", "items": [null, 17]}, "float32", "input_23"]}, "keras_version": "2.7.0", "backend": "tensorflow", "model_config": {"class_name": "Functional", "config": {"name": "model_11", "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 17]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "input_23"}, "name": "input_23", "inbound_nodes": [], "shared_object_id": 0}, {"class_name": "Dense", "config": {"name": "dense_99", "trainable": true, "dtype": "float32", "units": 32, "activation": {"class_name": "LeakyReLU", "config": {"name": "leaky_re_lu_22", "trainable": true, "dtype": "float32", "alpha": 0.0024999999441206455}, "shared_object_id": 1}, "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}, "shared_object_id": 2}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 3}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "name": "dense_99", "inbound_nodes": [[["input_23", 0, 0, {}]]], "shared_object_id": 4}, {"class_name": "Dense", "config": {"name": "dense_100", "trainable": true, "dtype": "float32", "units": 25, "activation": {"class_name": "LeakyReLU", "config": {"name": "leaky_re_lu_23", "trainable": true, "dtype": "float32", "alpha": 0.001500000013038516}, "shared_object_id": 5}, "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}, "shared_object_id": 6}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 7}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "name": "dense_100", "inbound_nodes": [[["input_23", 0, 0, {}]]], "shared_object_id": 8}, {"class_name": "BatchNormalization", "config": {"name": "batch_normalization_22", "trainable": true, "dtype": "float32", "axis": [1], "momentum": 0.99, "epsilon": 0.001, "center": true, "scale": true, "beta_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 9}, "gamma_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 10}, "moving_mean_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 11}, "moving_variance_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 12}, "beta_regularizer": null, "gamma_regularizer": null, "beta_constraint": null, "gamma_constraint": null}, "name": "batch_normalization_22", "inbound_nodes": [[["dense_99", 0, 0, {}]]], "shared_object_id": 13}, {"class_name": "BatchNormalization", "config": {"name": "batch_normalization_23", "trainable": true, "dtype": "float32", "axis": [1], "momentum": 0.99, "epsilon": 0.001, "center": true, "scale": true, "beta_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 14}, "gamma_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 15}, "moving_mean_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 16}, "moving_variance_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 17}, "beta_regularizer": null, "gamma_regularizer": null, "beta_constraint": null, "gamma_constraint": null}, "name": "batch_normalization_23", "inbound_nodes": [[["dense_100", 0, 0, {}]]], "shared_object_id": 18}, {"class_name": "Concatenate", "config": {"name": "concatenate_11", "trainable": true, "dtype": "float32", "axis": -1}, "name": "concatenate_11", "inbound_nodes": [[["batch_normalization_22", 0, 0, {}], ["batch_normalization_23", 0, 0, {}]]], "shared_object_id": 19}, {"class_name": "Dense", "config": {"name": "dense_101", "trainable": true, "dtype": "float32", "units": 20, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}, "shared_object_id": 20}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 21}, "kernel_regularizer": {"class_name": "L2", "config": {"l2": 0.009999999776482582}, "shared_object_id": 22}, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "name": "dense_101", "inbound_nodes": [[["concatenate_11", 0, 0, {}]]], "shared_object_id": 23}, {"class_name": "Dense", "config": {"name": "dense_102", "trainable": true, "dtype": "float32", "units": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}, "shared_object_id": 24}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 25}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "name": "dense_102", "inbound_nodes": [[["dense_101", 0, 0, {}]]], "shared_object_id": 26}], "input_layers": [["input_23", 0, 0]], "output_layers": [["dense_102", 0, 0]]}}, "training_config": {"loss": "mean_absolute_error", "metrics": [[{"class_name": "MeanMetricWrapper", "config": {"name": "mean_squared_logarithmic_error", "dtype": "float32", "fn": "mean_squared_logarithmic_error"}, "shared_object_id": 29}]], "weighted_metrics": null, "loss_weights": null, "optimizer_config": {"class_name": "Adam", "config": {"name": "Adam", "learning_rate": 0.0010000000474974513, "decay": 0.0, "beta_1": 0.8999999761581421, "beta_2": 0.9990000128746033, "epsilon": 1e-07, "amsgrad": false}}}}2
�root.layer-0"_tf_keras_input_layer*�{"class_name": "InputLayer", "name": "input_23", "dtype": "float32", "sparse": false, "ragged": false, "batch_input_shape": {"class_name": "__tuple__", "items": [null, 17]}, "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 17]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "input_23"}}2
�	root.layer_with_weights-0"_tf_keras_layer*�{"name": "dense_99", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "Dense", "config": {"name": "dense_99", "trainable": true, "dtype": "float32", "units": 32, "activation": {"class_name": "LeakyReLU", "config": {"name": "leaky_re_lu_22", "trainable": true, "dtype": "float32", "alpha": 0.0024999999441206455}, "shared_object_id": 1}, "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}, "shared_object_id": 2}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 3}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "inbound_nodes": [[["input_23", 0, 0, {}]]], "shared_object_id": 4, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 17}}, "shared_object_id": 30}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 17]}}2
�	root.layer_with_weights-1"_tf_keras_layer*�{"name": "dense_100", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "Dense", "config": {"name": "dense_100", "trainable": true, "dtype": "float32", "units": 25, "activation": {"class_name": "LeakyReLU", "config": {"name": "leaky_re_lu_23", "trainable": true, "dtype": "float32", "alpha": 0.001500000013038516}, "shared_object_id": 5}, "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}, "shared_object_id": 6}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 7}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "inbound_nodes": [[["input_23", 0, 0, {}]]], "shared_object_id": 8, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 17}}, "shared_object_id": 31}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 17]}}2
�	root.layer_with_weights-2"_tf_keras_layer*�	{"name": "batch_normalization_22", "trainable": true, "expects_training_arg": true, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "BatchNormalization", "config": {"name": "batch_normalization_22", "trainable": true, "dtype": "float32", "axis": [1], "momentum": 0.99, "epsilon": 0.001, "center": true, "scale": true, "beta_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 9}, "gamma_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 10}, "moving_mean_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 11}, "moving_variance_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 12}, "beta_regularizer": null, "gamma_regularizer": null, "beta_constraint": null, "gamma_constraint": null}, "inbound_nodes": [[["dense_99", 0, 0, {}]]], "shared_object_id": 13, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": 2, "max_ndim": null, "min_ndim": null, "axes": {"1": 32}}, "shared_object_id": 32}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 32]}}2
�	root.layer_with_weights-3"_tf_keras_layer*�	{"name": "batch_normalization_23", "trainable": true, "expects_training_arg": true, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "BatchNormalization", "config": {"name": "batch_normalization_23", "trainable": true, "dtype": "float32", "axis": [1], "momentum": 0.99, "epsilon": 0.001, "center": true, "scale": true, "beta_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 14}, "gamma_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 15}, "moving_mean_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 16}, "moving_variance_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 17}, "beta_regularizer": null, "gamma_regularizer": null, "beta_constraint": null, "gamma_constraint": null}, "inbound_nodes": [[["dense_100", 0, 0, {}]]], "shared_object_id": 18, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": 2, "max_ndim": null, "min_ndim": null, "axes": {"1": 25}}, "shared_object_id": 33}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 25]}}2
�root.layer-5"_tf_keras_layer*�{"name": "concatenate_11", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "Concatenate", "config": {"name": "concatenate_11", "trainable": true, "dtype": "float32", "axis": -1}, "inbound_nodes": [[["batch_normalization_22", 0, 0, {}], ["batch_normalization_23", 0, 0, {}]]], "shared_object_id": 19, "build_input_shape": [{"class_name": "TensorShape", "items": [null, 32]}, {"class_name": "TensorShape", "items": [null, 25]}]}2
�root.layer_with_weights-4"_tf_keras_layer*�{"name": "dense_101", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "Dense", "config": {"name": "dense_101", "trainable": true, "dtype": "float32", "units": 20, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}, "shared_object_id": 20}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 21}, "kernel_regularizer": {"class_name": "L2", "config": {"l2": 0.009999999776482582}, "shared_object_id": 22}, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "inbound_nodes": [[["concatenate_11", 0, 0, {}]]], "shared_object_id": 23, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 57}}, "shared_object_id": 34}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 57]}}2
�root.layer_with_weights-5"_tf_keras_layer*�{"name": "dense_102", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "Dense", "config": {"name": "dense_102", "trainable": true, "dtype": "float32", "units": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}, "shared_object_id": 24}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 25}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "inbound_nodes": [[["dense_101", 0, 0, {}]]], "shared_object_id": 26, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 20}}, "shared_object_id": 35}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 20]}}2
�$root.layer_with_weights-0.activation"_tf_keras_layer*�{"name": "leaky_re_lu_22", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "LeakyReLU", "config": {"name": "leaky_re_lu_22", "trainable": true, "dtype": "float32", "alpha": 0.0024999999441206455}, "shared_object_id": 1}2
�$root.layer_with_weights-1.activation"_tf_keras_layer*�{"name": "leaky_re_lu_23", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "class_name": "LeakyReLU", "config": {"name": "leaky_re_lu_23", "trainable": true, "dtype": "float32", "alpha": 0.001500000013038516}, "shared_object_id": 5}2
�troot.keras_api.metrics.0"_tf_keras_metric*�{"class_name": "Mean", "name": "loss", "dtype": "float32", "config": {"name": "loss", "dtype": "float32"}, "shared_object_id": 36}2
�uroot.keras_api.metrics.1"_tf_keras_metric*�{"class_name": "MeanMetricWrapper", "name": "mean_squared_logarithmic_error", "dtype": "float32", "config": {"name": "mean_squared_logarithmic_error", "dtype": "float32", "fn": "mean_squared_logarithmic_error"}, "shared_object_id": 29}2