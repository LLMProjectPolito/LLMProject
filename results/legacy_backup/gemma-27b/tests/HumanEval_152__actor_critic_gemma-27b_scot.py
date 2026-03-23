# ERROR: 2 validation errors for ChatOpenAI
callbacks.list[is-instance[BaseCallbackHandler]].0
  Input should be an instance of BaseCallbackHandler [type=is_instance_of, input_value=<src.utils.model_registry...t at 0x000001AB22153D50>, input_type=TokenCounter]
    For further information visit https://errors.pydantic.dev/2.11/v/is_instance_of
callbacks.is-instance[BaseCallbackManager]
  Input should be an instance of BaseCallbackManager [type=is_instance_of, input_value=[<src.utils.model_registr... at 0x000001AB22153D50>], input_type=list]
    For further information visit https://errors.pydantic.dev/2.11/v/is_instance_of