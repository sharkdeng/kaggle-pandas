
# freeze layers in pytorch
def freeze_until(model, name):
     flag = False
     for n, p in model.named_parameters():
         if n == name:
             flag = True
         p.requires_grad = flag
freeze_until(model, 'model.layer4.2.conv1.weight')
