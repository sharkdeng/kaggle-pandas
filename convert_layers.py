
# Replace BatchNorm with GroupNorm
def convert_layers(model, old_layer_type, new_layer_type, convert_weights=False, num_groups=None):
    
    for name, module in reversed(model._modules.items()):
    
        if len(list(module.children())) > 0:
            # recurse
            model._modules[name] = convert_layers(module, old_layer_type, new_layer_type, convert_weights, num_groups=num_groups)

        # single module
        if type(module) == old_layer_type:
            old_layer = module
            new_layer = new_layer_type(module.num_features if num_groups is None else num_groups, module.num_features, module.eps, module.affine)

            if convert_weights:
                new_layer.weight = old_layer.weight
                new_layer.bias = old_layer.bias

            model._modules[name] = new_layer

    return model
