vp_sandbox={}
vp_sandbox_mode=False
protect=["vp","variablesplus","vp_sandbox","vp_sandbox_mode"]
def variables_plus(cmd):
    global vp_sandbox, vp_sandbox_mode
    cmd=cmd.strip()
    a=""
    b=""
    c=""
    if cmd.startswith("clear(") and cmd.endswith(")"):
        if not vp_sandbox_mode:
            if cmd[6:-1] == "":
                for i in globals():
                    if not i.startswith("__") and not callable(globals()[i]) and not i.startswith("<function") and i not in protect:
                        globals()[i]=""
            else:
                try:
                    for i in globals():
                        if not i.startswith("__") and not callable(globals()[i]) and not i.startswith("<function") and i not in protect:
                            if i==cmd[6:-1]:
                                globals()[i]=""
                except Exception:
                    raise TypeError("Invalid variable! Enter a variables name or leave it blank to clear the variable(s).")
        else:
            if cmd[6:-1] == "":
                for i in vp_sandbox:
                    vp_sandbox[i]=""
            else:
                try:
                    vp_sandbox[cmd[6:-1]]=""
                except Exception:
                    raise TypeError("Invalid variable! Enter a variables name or leave it blank to clear the variable(s).")
    elif cmd.startswith("create(") and cmd.endswith(")"):
        if not vp_sandbox_mode:
            if not cmd[7:-1] == "":
                try:
                    if "=" in cmd[7:-1]:
                        a,b=cmd[7:-1].split("=", 1)
                        if not a in globals():
                            globals()[a]=b
                        else:
                            raise SyntaxError("Variable "+a+" already exists! Use vp.vp('write()') to modify a variable's contents.")
                    else:
                        a=cmd[7:-1]
                        if not a in globals():
                            globals()[a]=""
                        else:
                            raise SyntaxError("Variable "+a+" already exists! Use vp.vp('write()') to modify a variable's contents.")
                except Exception:
                    raise TypeError("Invalid format. Use name=value.")
            else:
                raise TypeError("You can't create a blank variable.")
        else:
            if not cmd[7:-1] == "":
                try:
                    if "=" in cmd[7:-1]:
                        a,b=cmd[7:-1].split("=", 1)
                        if not a in vp_sandbox:
                            vp_sandbox[a]=b
                        else:
                            raise SyntaxError("Variable "+a+" already exists! Use vp.vp('write()') to modify a variable's contents.")
                    else:
                        a=cmd[7:-1]
                        if not a in vp_sandbox:
                            vp_sandbox[a]=""
                        else:
                            raise SyntaxError("Variable "+a+" already exists! Use vp.vp('write()') to modify a variable's contents.")
                except Exception:
                    raise TypeError("Invalid format. Use name=value.")
            else:
                raise TypeError("You can't create a blank variable.")
    elif cmd.startswith("delete(") and cmd.endswith(")"):
        if not vp_sandbox_mode:
            if not cmd[7:-1] == "":
                for i in globals():
                    if not i.startswith("__") and not callable(globals()[i]) and i not in protect:
                        if i==cmd[7:-1]:
                            try:
                                del globals()[i]
                                break
                            except Exception:
                                raise TypeError("Variable", i, "doesn't exist.")
            else:
                raise SyntaxError("You can't delete a non-existent variable.")
        else:
            if not cmd[7:-1] == "":
                for i in vp_sandbox:
                    if i==cmd[7:-1]:
                        try:
                            del vp_sandbox[i]
                            break
                        except Exception:
                            raise TypeError("Variable", i, "doesn't exist.")
            else:
                raise SyntaxError("You can't delete a non-existent variable.")
    elif cmd.startswith("read(") and cmd.endswith(")"):
        if not vp_sandbox_mode:
            if cmd[5:-1] in globals():
                return globals()[cmd[5:-1]]
            else:
                raise TypeError("Variable", cmd[5:-1], "doesn't exist.")
        else:
            if cmd[5:-1] in vp_sandbox:
                return vp_sandbox[cmd[5:-1]]
            else:
                raise TypeError("Variable", cmd[5:-1], "doesn't exist.")
    elif cmd.startswith("write(") and cmd.endswith(")"):
        if not vp_sandbox_mode:
            if not cmd[6:-1] == "":
                try:
                    if "=" in cmd[6:-1]:
                        a,b=cmd[6:-1].split("=", 1)
                        if a in globals():
                            globals()[a]=b
                        else:
                            raise SyntaxError("Variable "+a+" doesn't exist! Use vp.vp('create()') to create a new variable.")
                    else:
                        a=cmd[6:-1]
                        raise SyntaxError("To modify variable "+a+", you must use '=' .")
                except Exception:
                    raise TypeError("Invalid format. Use name=value.")
            else:
                raise TypeError("You can't modify a non-existent variable.")
        else:
            if not cmd[6:-1] == "":
                try:
                    if "=" in cmd[6:-1]:
                        a,b=cmd[6:-1].split("=", 1)
                        if a in vp_sandbox:
                            vp_sandbox[a]=b
                        else:
                            raise SyntaxError("Variable "+a+" doesn't exist! Use vp.vp('create()') to create a new variable.")
                    else:
                        a=cmd[6:-1]
                        raise SyntaxError("To modify variable "+a+", you must use '=' .")
                except Exception:
                    raise TypeError("Invalid format. Use name=value.")
            else:
                raise TypeError("You can't modify a non-existent variable.")
    elif cmd.startswith("SANDBOX(") and cmd.endswith(")"):
        if cmd[8:-1]=="1" or cmd[8:-1].lower()=="true":
            vp_sandbox_mode=True
        elif cmd[8:-1]=="0" or cmd[8:-1].lower()=="false":
            vp_sandbox_mode=False
        else:
            raise SyntaxError("You must enter 0, 1, True or False to toggle the sandbox mode.")
    else:
        raise TypeError("Invalid command! Use vp.vp('clear()'), vp.vp('create()'), vp.vp('write()'), vp.vp('SANDBOX()') or vp.vp('delete()').")
vp=variables_plus
