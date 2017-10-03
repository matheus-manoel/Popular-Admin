def get_missing_params(params, obligatory_params):
    missing_params = [param for param in params if param not in obligatory_params]
    return missing_params
