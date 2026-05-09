def replay(method):
    """
    Displays the history of calls of a particular function.
    """
    # Redis obyektinə metod vasitəsilə çatırıq
    self_redis = method.__self__._redis
    method_name = method.__qualname__
    
    # Giriş və çıxış açarlarını tapırıq
    inputs_key = "{}:inputs".format(method_name)
    outputs_key = "{}:outputs".format(method_name)
    
    # Redis-dən bütün tarixçəni çəkirik
    inputs = self_redis.lrange(inputs_key, 0, -1)
    outputs = self_redis.lrange(outputs_key, 0, -1)
    
    # Neçə dəfə çağırıldığını çap edirik
    print("{} was called {} times:".format(method_name, len(inputs)))
    
    # inputs və outputs üzərində eyni anda dövr edirik
    for inp, out in zip(inputs, outputs):
        # Redis-dən gələn byte-ları decode edirik
        input_str = inp.decode("utf-8")
        output_str = out.decode("utf-8")
        
        print("{}(*({})) -> {}".format(method_name, input_str, output_str))
