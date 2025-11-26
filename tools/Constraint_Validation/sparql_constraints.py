
# These strings make up SPARQL queries that, when run, will return the classes which violate the constraint.

CONSTRAINT_SPARQL_PREFIX = ''' 
add some prefixes here...
'''

QUERY_KIND_C1 = (
    CONSTRAINT_SPARQL_PREFIX
    + """
    SELECT DISTINCT ?kind_class
    WHERE {
    ?kind_class ontouml:stereotype ontouml:kind ;
    ontouml:specific+ ?superClass .
    ?superClass gist:isCategorizedBy gistx:__ProvidesIdentity_True__ .
    """
    )

QUERY_KIND_C2= (
    CONSTRAINT_SPARQL_PREFIX
    + """
    SELECT DISTINCT ?kind_class
    WHERE {
    ?kind_class ontouml:stereotype ontouml:kind ;
    ontouml:specific+ ?superClass .
    ?superClass gist:isCategorizedBy gistx:__ProvidesIdentity_True__ .
    """
)

QUERY_KIND_C3= (
    CONSTRAINT_SPARQL_PREFIX
    + """
    SELECT DISTINCT ?kind_class
    WHERE {
    ?kind_class ontouml:stereotype ontouml:kind ;
    ontouml:specific+ ?superClass .
    ?superClass gist:isCategorizedBy gistx:__IdentityPrinciple_Multiple__ .
    """
)

QUERY_KIND_C4= (
    CONSTRAINT_SPARQL_PREFIX
    + """
    SELECT DISTINCT ?kind_class
    WHERE {
    ?kind_class ontouml:stereotype ontouml:kind ;
    ontouml:specific+ ?superClass .
    ?superClass gist:isCategorizedBy gistx:__Rigidity_AntiRigid__ .
    """
)


