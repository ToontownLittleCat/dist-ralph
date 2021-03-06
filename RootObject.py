from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal

class RootObject(DistributedObjectGlobal):
    """ This 'dummy' object may not look like much, 
    but it *is* important internally.

    Almost *all* objects needs a parent, and this object
    will be the parent to the 'LoginManager' and all
    the 'World' objects. (But not the Ralph avatars, they'll be parented to the world itself)
    And without this object's existance, Astron wouldn't be able to 
    parent the objects correctly, and it wouldn't be able direct the client's 
    inital interest messages.  Therefore, the client wouldn't receive 
    the 'World' objects as a result.

    (The client does not need this object's existance, but we need a 
    dummy class here to prevent an import error while reading the DC files.)
    """
    
    pass