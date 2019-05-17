

class ConstantValues:

    # User model constants
    BEGINNER = 5
    INTERMEDIATE = 4
    ADVANCED = 3

    TIMEOUT = 10

    MAX_SUBMODULARITY = 5000
    MAXSIZE = 23000
    BUDGET = 100
    Lambda = 1.0
    Alpha = 0.8
    #SIMILARITY_MEASUE='title'
    #SIMILARITY_MEASUE='abstract'
    SIMILARITY_MEASUE = 'text'
    # ACL_CORPUS_INDEX = "acl_tfidf"
    ACL_CORPUS_INDEX = "acl_bm25"
    ACL_CORPUS_DOCTYPE = "doc"
    OneVsRest = "OneVsRest"

    LAZY_GREEDY_ALG=0 #default
    COSINE = 0 #default

    #method
    Maximal_Marginal_Relevance = "mmr"
    Maximal_Concept_Relevance = "mcr"
    Query_Focused_Relevance = "qfr"
    Update_Relevance = "upr"

    #data path
    SAMPLE="sample/"
    ACL = "../data/acl/"
    ACL_PART = "../data/acl-part/"
    # ACL_SCORES = "../data/acl-score/"
    ACL_SCORES = "../data/acl-bm25-score/"
    # SAMPLE_SCORES = "sample-bm25-score/"

    #save model
    DICTIONARY = "acl.dict"
    CORPUS = "acl.mm"
    TFIDF_INDEX = "tfidf.index"
    DOCSIMS = "docsims.json"

    #evaluation
    OUTPUT_KEY = "output"
    ANSWER_KEY = "references"