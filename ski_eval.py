import src.ski as ski

##########
# PART 1 #
##########
# TASK: Implement the below function `eval`.
    
def eval(e: ski.Expr) -> ski.Expr:
    if isinstance(e, ski.App):
        e1 = eval(e.e1)
        # Don't greedily evaluate e2 in case it infinite loops

        # I x with format e1 e2
        if isinstance(e1, ski.I):
            return eval(e.e2)

        # (K x) y with format (e1.e1 e1.e2) e2
        if isinstance(e1, ski.App) and isinstance(e1.e1, ski.K):
            return eval(e1.e2)

        # ((S x) y) z with format ((e1.e1.e1 e1.e1.e2) e1.e2) e2
        if isinstance(e1, ski.App) and isinstance(e1.e1, ski.App) and isinstance(e1.e1.e1, ski.S): 
            x = e1.e1.e2
            y = e1.e2
            z = eval(e.e2)
            return eval(ski.App(ski.App(x, z), ski.App(y, z)))

        else: 
            return ski.App(e1, eval(e.e2))

    else: # can't do anything if there's no application
        return e