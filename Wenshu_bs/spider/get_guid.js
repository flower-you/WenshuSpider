function createGuid()
{return(((1+Math.random())*65536)|0).toString(16).substring(1)
}
function getGuid() {
    return guid = createGuid() + createGuid() + "-" + createGuid() + "-" + createGuid() + createGuid() + "-" + createGuid() + createGuid() + createGuid();
}