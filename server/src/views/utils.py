def get_missing_params(params, obligatory_params):
    missing_params = [param for param in obligatory_params if param not in params]
    return missing_params
