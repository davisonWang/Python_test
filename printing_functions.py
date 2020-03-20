# 首先创建一个列表，其中包含要打印的设计
def print_models(unprinted_model, completed_model):
    """模拟打印每个涉及，直到没有未打印的设计为止
     打印每个设计后，都将其移到列表completed_models中"""
    while unprinted_model:
        current_list = unprinted_model.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing Models: -" + current_list)
        completed_model.append(current_list)
print("-------------------------------------------------------------------------------")

def show_print_models(completed_model):
    """显示打印好的所有模型"""
    for completed_models in completed_model:
        message = completed_models.title()
        print(message)

