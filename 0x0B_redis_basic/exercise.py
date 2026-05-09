def replay(method):
    """
    Displays the history of calls of a particular function.
    """
    import redis
    # Metodun aid olduğu klassın daxilindəki redis instansiyasına çatırıq
    r = method.__self__._redis
    # Metodun tam adını alırıq (məsələn: Cache.store)
    m_name = method.__qualname__
    
    # Açar adlarını müəyyən edirik
    in_key = "{}:inputs".format(m_name)
    out_key = "{}:outputs".format(m_name)
    
    # Məlumatları Redis-dən çəkirik
    inputs = r.lrange(in_key, 0, -1)
    outputs = r.lrange(out_key, 0, -1)
    
    # İlk sətri çap edirik
    print("{} was called {} times:".format(m_name, len(inputs)))
    
    # zip ilə hər iki siyahını eyni anda oxuyuruq
    for inp, out in zip(inputs, outputs):
        # Redis-dən gələn məlumatlar byte formatındadır, decode edirik
        # Input artıq "('foo',)" kimi string formatında yadda saxlanılıb
        print("{}(*({})) -> {}".format(
            m_name,
            inp.decode("utf-8"),
            out.decode("utf-8")
        ))
