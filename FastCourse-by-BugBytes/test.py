from typing import Annotated,get_args,get_type_hints,get_origin

def double(x: Annotated[int,(0.100)])->int:
    type_hints = get_type_hints(double,include_extras=True)
    hint = type_hints['x']
    if get_origin(hint) is Annotated:
        hint_type,*hint_args = get_args(hint)
        print(hint_type)
        print(hint_args)
    print(hint)    
    return x*2

resulte = double(4)
print(resulte)

# FastAPI  uses annotaions to add metadata to request params