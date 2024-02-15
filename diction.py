def count_firstperson(text):
    firstperson={
     "i","me","my","myself","mine"
     }
    count=0
    for i in text.split():
        if i.lower() in firstperson:
            count+=1

    return count    

def compliance(text):
    compliance = {
    "compliance", "compliant", "legal", "legalized", "legally", "legality", "regulate", "regulated", "regulates",
    "regulation", "regulatory", "risk", "risks"
    }

    count = 0 
    p=0
    for word in text.split():
        p+=1
        if word.lower() in compliance:
            count += 1

    return count/p *100

def buisness(text):
    buisness = {
    "biotechnolog", "biotechnology", "biotechnologies", "costs", "costly", "costing", "costed", "cost benefits",
    "customers", "demanding", "demands", "efficiency", "efficiencies", "expense", "expenses", "markets", "marketing",
    "market shares", "market values", "profits", "rpfited", "profiting", "profitable", "profitability", "roi",
    "strategy", "strategies", "strategic", "strategical", "strategically", "technology", "technologies", "value chains",
    "business as usual", "business model", "competitive advantage", "cost", "cost benefit", "customer", "demand",
    "efficienc", "market", "market share", "market value", "money", "profit", "public relations", "retention",
    "return on investment", "sales", "strateg", "value chain", "technolog"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in buisness:
            count += 1

    return count/p *100

def systemic(text):
    systemic = {
    "collaborate", "collaborates", "collaborated", "collaborating", "collaborative", "cooperate", "cooperated",
    "cooperating", "cooperation", "cooperative", "cooperatives", "ecoefficiency", "ecoefficiencies", "game changer",
    "game changing", "global citizen", "global citizens", "global citizenship", "humanity", "industry", "integrate",
    "integrates", "integrating", "integration", "integrative", "partnership", "partnerships", "system", "systens",
    "systemic", "transform", "transforms", "transformed", "transforming", "transformation", "transformations",
    "transformative"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in systemic:
            count += 1

    return count/p *100

def regenerative(text):
    regenerative = {
    "carrying capacity", "consumption", "degrowth", "holistic", "interdependent", "interdependence", 
    "interdependencies", "natural system", "natural systems", "planetary boundary", "planetary boundaries", 
    "preservation", "redistribution", "repair", "repairs", "repairing", "repaired", "restore", "restored", 
    "restores", "restoring", "restoration", "restorative", "science", "sciences", "scientific", "steady state", 
    "steady states", "zero growth"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in regenerative:
            count += 1

    return count/p *100

def coevo(text):
    coevo = {
    "circular", "coevolve", "coevolving", "coevolution", "ecocentric", "ecocentrics", "ecocentrism", 
    "ecoethic", "ecoethics", "ecological", "ecology", "ecosystem", "ecosystems", "flourish", "flourished", 
    "flourishes", "flourishing", "no growth", "regenerate", "regenerated", "regenerating", "regeneration", 
    "regenerative", "resilience", "resilient"}

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in coevo:
            count += 1

    return count/p *100

def innovation(text):
    innovation = {
    "actualize", "adapt", "advanc", "artistic", "avant-garde", "best-in-class", "brainstorm", "build", "change",
    "clever", "conceiv", "contemporary", "craz", "create", "cutting-edge", "depart", "design", "develop", "device",
    "devis", "differ", "discover", "efficien", "enhanc", "enterprising", "expand", "experiment", "forge", "form",
    "found", "fresh", "future", "generat", "ground-breaking", "grow", "hatch", "imagin", "improv", "individual",
    "industry-leading", "ingen", "initiat", "innovate", "inspire", "introduce", "invent", "lead", "leading-edge",
    "metamorphosis", "modern", "modif", "new", "novel", "odd", "offbeat", "open-mind", "opportunity", "origin",
    "peculiar", "pioneer", "problem-solv", "produc", "prolific", "radical", "resourceful", "revolution", "set up",
    "shift", "solv", "spawn", "state-of-the-art", "surpris", "trailblaz", "transform", "uncommon", "unfamiliar",
    "unique", "unprecedent", "unusual", "unveil", "upheav", "vicissitude", "vision", "wild"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in innovation:
            count += 1

    return count/p *100

def supplychain(text):
    supplychain={
     "integrity","product","value","customer","concern","government","health","collegue","global","decision","community","person","help","line",
     "respect"
     }
    count=0
    p=0
    for i in text.split():
        p+=1
        if i.lower() in supplychain:
            count+=1

    return count/p *100

def governanceparties(text):
    governanceparties={
     "officer","associate","director","financial","board","gift","member","regulation","committee","disclosure","counsel","executive","chief",
     "situation","opportunity"
     }
    count=0
    p=0
    for i in text.split():
        p+=1
        if i.lower() in governanceparties:
            count+=1

    return count /p *100

def riskfactors(text):
    riskfactors={
     "customer","question","concern","government","product","gift","entertainment","member","supervisor","contact","competitor","supplier","value",
     "material","integrity"
     }
    count=0
    p=0
    for i in text.split():
        p+=1
        if i.lower() in riskfactors:
            count+=1

    return count/p *100

def governmentcontracting(text):
    governmentcontracting={
     "office","official","partner","government","contact","gift","contract","party","service","approval","time","supplier","security",
     "financial","integrity"
     }
    count=0
    p=0
    for i in text.split():
        p+=1
        if i.lower() in governmentcontracting:
            count+=1

    return count/p *100

def riskcontrol(text):
    riskcontrol={
    "energy", "supervisor", "customer", "contact", "service", "employment", "gift", "safety", "security", "public", 
    "time", "health", "question", "workplace", "concern"
    }
    count=0
    p=0
    for i in text.split():
        p+=1
        if i.lower() in riskcontrol:
            count+=1

    return count/p *100

def thirdparty(text):
    thirdparty={
     "client","outside","employment","customer","public","gift","bank","page","service","transaction","political","region","security",
     "financial","approval"
     }
    count=0
    p=0
    for i in text.split():
        p+=1
        if i.lower() in thirdparty:
            count+=1

    return count/p 

def personatrisk(text):
    personatrisk={
     "officer","government","director","employment","customer","regulation","security","material","appropriate","procedure","practice","foreign","service",
     "official","payment"
     }
    count=0
    p=0
    for i in text.split():
        p+=1
        if i.lower() in personatrisk:
            count+=1

    return count/p *100

def count_healthcare(text):
    healthcare = {
        "team", "patient", "global", "member", "healthcare",
        "question", "service", "page", "product", "pre", "partner", "met",
        "professional", "value", "local"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in healthcare:
            count += 1

    return count/p *100

def igh(text):
    igh = {
        "value", "customer", "concern", "contact", "person",
        "help", "decision", "global", "community", "team", "commitment", "safety",
        "practice", "integrity", "question"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in igh:
            count += 1

    return count/p *100

def investigativesystem(text):
    investigativesystem = {
        "product", "supplier", "gift", "safety", "human",
        "harassment", "question", "local", "payment", "hotline", "time", "unemployment",
        "property", "environment", "system"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in investigativesystem:
            count += 1

    return count/p*100

def board(text):
    board = {
    "accountability", "adding value", "authentic", "balanced board", "best practice", "board appraisal",
    "board diversity", "board engagement", "board skills", "champion of change", "commitment to change",
    "constant drive", "constructive", "corporate citizenship", "corporate conduct", "corporate responsibility",
    "corporate social investment", "critical thinking", "custodians", "debate", "director", "assessment",
    "discussion", "doing good", "doing the right thing", "esg", "ethical values", "ethics",
    "executive remuneration", "future fit organization", "good governance", "healthy tension", "independent oversight",
    "influence", "integrated governance", "integrated reporting", "integrated thinking", "integrity",
    "lasting change", "lasting contribution", "lead by example", "leadership ability", "leadership capability",
    "leadership development", "leadership skills", "legacy", "long term", "management", "governance practices",
    "mission statement", "moral compass", "passion", "pioneer", "policy", "positive impact", "principles",
    "prioritization", "prosperity", "purpose", "purpose driven", "reporting boundary", "reputation", "resilience",
    "respectful", "responsible", "safeguard", "self evaluation", "shared values", "skills matrix", "social good",
    "social license", "social centric", "stewardship", "succession plan", "sustainable development", "the right thing",
    "the right way", "tone at the top", "transparent", "trusted", "values", "values driven", "vision", "whistleblowing"
      }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in board:
            count += 1

    return count/p *100

def strategy(text):
    strategy = {
   
    "agility", "alignment", "alliance", "balanced decisions", "beneficial relationships", "benefit to society",
    "broad participation", "broaden horizons", "broader perspective", "broader societal impact", "business model capitals",
    "causal relationships", "common interest", "community", "consultation", "contribution to society", "creating value",
    "customer engagement", "dialogue", "effective engagement", "effective partnerships", "environmental capital",
    "environmental factors", "external engagement", "financial capital", "future generations", "future oriented",
    "good relations", "government engagement", "holistic approach", "human capital", "human centric", "impactful relationships",
    "incentive", "inclusive growth strategies", "innovation", "intangible assests", "intangible value", "integrated approach",
    "integrated business model", "integrated decisions", "integrated planning", "integrated stakeholder agreement",
    "integrated sustainability", "integrated value chain", "integrated view", "intellectual capital", "inter dependence",
    "long term", "manufactured capital", "material to stakeholders", "materiality", "multicapital perspective", "multiple capitals",
    "mutual collaboration", "mutually beneficial", "natural capital", "natural environment", "non financial capital", "oppurtunity",
    "optimal balance", "participation", "partnerships", "performance", "reward", "positive engagement", "public engagement",
    "purposeful", "range of stakeholders", "responsive risk", "robust business strategy", "robus relationships", "satisfied customers",
    "shared planning", "shared vision", "silent stakehokders", "social and relationship capital", "social capital", "social investment",
    "social value", "socially aware", "socially progressive", "stakeholder communications", "stakeholder consulation",
    "stakeholder dialogue", "stakeholder engagement", "stakeholder feedback", "stakeholder focus", "stakeholder inculsivity",
    "stakeholder interests", "stakeholder needs", "stakeholder participation", "stakeholder relationships", "stakeholder views",
    "stakeholder centric", "stakeholder inclusive", "strategic alignment", "strategic alliance", "strategic goals", "strategic mission",
    "strategic objectives", "strategic partnerships", "strategic plan", "strategic relationships", "strategic vision", "strategic alignment",
    "supply chain visibility", "sustainability", "sustainability goals", "trade offs", "two way communication", "value chain",
    "value co creation", "value drivers", "value based strategy", "value relevant", "wider society", "win win", "working relationships"


      }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in strategy:
            count += 1

    return count/p *100

def culture(text):
    culture={
    "attract talent", "attractiveness as an employer", "coaching", "cohesiveness", "collaboration", "colleagues", 
    "collective", "committed", "common values", "communication", "continous improvement", "continous learning", 
    "cooperative", "core skills", "cultural shift", "cultural transformation", "cultural values", "diversity", 
    "education", "emotional support", "employee engagement", "employee experience", "employee forum", 
    "employee incentive", "employee involvement", "employee ownership", "employee rights", "employee value proposition", 
    "employee centric", "employee equity", "empowerment", "encourgement", "encouragement", "equal oppurtunities", 
    "equitable", "fair pay", "feedback", "healthy", "honesty", "humanity", "humbleness", "inclusive", 
    "interpersonal relationships", "investing in employees", "knowledge sharing", "learning oppurtunities", 
    "learning organization", "listening", "long term incentive plan", "long tern retention plan", 
    "low staff turnover", "loyalty", "mentoring", "merit based", "minimize harm", "nurturing", "openness", 
    "people centered", "personal accountability", "positive working environment", "proactivity", "productive", 
    "reskilling respect", "reward and recognition", "role based pay", "safe production", "shared capabilities", 
    "shared goals", "shared intelligence", "shared knowledge", "shared ownership", "sharing expertise", 
    "skills development", "social interactions", "stable workforce", "supportive", "talent management", 
    "talent metrics", "talent pipline", "talent retention", "talented people", "talented workforce", 
    "team coehsion", "team development", "team dynamics", "team effectiviness", "team engagement", "team goals", 
    "team outputs", "team performance", "teambuilding", "teamwork", "training", "transformation metrics", 
    "transformed workforce", "transparency", "trust", "trust building", "up skilling", "value driven", "culture", 
    "ways of working", "wellbeing", "zero harm"
    }
    count=0
    p=0
    for i in text.split():
        p+=1
        if i.lower() in culture:
            count+=1

    return count/p *100



def info(text):
    info = {
    "access knowledge", "accounting infrastructure", "accounting system", "advanced analytics", "agile", "analysis",
    "assessing performance", "assurance", "audit", "balanced scorecard", "breaking down silos", "broader performance",
    "business unit collaboration", "business partnering", "business scorecard", "comparable measures", "connectivity",
    "consistent measurement systems", "controls", "credibility", "cross functional", "dashboards", "data accuracy",
    "data analytics", "data driven insights", "decentralized", "decision making systems", "department liasion",
    "design thinking", "effeciencies", "functional integration", "future looking information", "future oriented information",
    "high quality data", "improving systems", "information flow", "information process", "information quality",
    "information systems", "insight driven decisions", "integrated indicators", "integrated information",
    "integrated measures systems", "integrated measures", "integrated metrics", "integrated performance", "integrated process",
    "interfucntional", "internal control", "kpis", "lean", "management information systems", "measurement tool",
    "measuring value", "metrics", "multidisciplinary teams", "multiple objectives", "non financial indicators",
    "organizational competencies", "organizational integration", "organizational restructure", "overcome boundaries",
    "perfornance indicators", "performance measurement systems", "performance scorecard", "qualitative factors",
    "reduce duplication", "relevant objectives", "targets", "reliable information", "reporting protocols", "rigor",
    "robus measures", "silos mentality", "siloed thinking", "synergies", "streamline", "systems thinking",
    "technology platforms", "transformation agenda", "veracity of systems"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in info:
            count += 1

    return count/p *100

def fraud(text):
    fraud = {
    "slump", "disturb", "trigger", "brew", "trouble", "special", "consolidate", "improve", "overclocking", "cause",
    "launch", "universal", "provision", "adjust", "active", "integrate", "turning", "not smooth", "recession",
    "stable", "dedicate", "burst", "subvert", "cross industry", "strict", "deviation", "excellent", "major",
    "reasonable", "toil", "expect", "boom", "support", "noise", "deferred", "move", "pleasant stages", "stabilized",
    "not reach", "resolution", "conservative", "gap", "huge", "forecast", "competition", "economize", "dilemma",
    "looking for", "cautious", "underprice", "rise", "priate edition", "unite efforts", "saturation", "shift",
    "sharp", "micro profit", "remain high", "decline", "optimistic", "backlog", "very deep", "attack", "calm down",
    "dispersion", "exploit", "damag", "optimization", "see through", "stimulate", "change", "reach", "committed",
    "cooperation", "reduce", "strive for", "insufficient", "low", "excitation", "rebound", "step by step", "ensure",
    "complete", "reduce", "spare no efforts", "anew", "roughly", "deep", "control", "review", "break out", "timely",
    "sound", "different", "request", "extend", "strength", "strongly", "pursue", "strengthen", "original",
    "oppurtunity", "fluctuation", "situation", "focus on", "only", "face", "not yet", "extended", "firm", "timely",
    "no burden", "regret", "stride forward", "estimate", "difficult", "transfer", "conspiracy", "enlarge", "repay",
    "in depth", "foothhold", "focus", "improve", "interplant transfer", "injection", "highlight", "weak", "unfavorable",
    "issue", "avoid", "superior", "in response", "event", "rescue", "early", "differentiation", "hold", "bad", "create",
    "pull down", "aggravate", "serious", "solve", "overall", "in private", "required", "turn to", "not as good as",
    "impact"
    }

    count = 0
    p=0
    for word in text.split():
        p+=1
        if word.lower() in fraud:
            count += 1

    return count/p *100

# Read text from the file
file_path = "D:\Omkar\Downloads\SPJIMR\Coforge.txt"
with open(file_path, 'r',encoding='utf8') as file:
    text = file.read()

print("Total words: ",file_path.split())

#Count firstperson pronouns
count_firstperson=count_firstperson(text)
print("Firstperson: ",count_firstperson)

#Count compliance
count_compliance=compliance(text)
print(count_compliance)
#Count BuisnessCentered
count_buisness=buisness(text)
print(count_buisness)
#Count Systemic
count_systemic=systemic(text)
print(count_systemic)
#Count Regenerative
count_regenerative=regenerative(text)
print(count_regenerative)
#Count Coevo
count_coevo=coevo(text)
print(count_coevo)
# Count Innovation and creativity
count_innovation = innovation(text)
print( count_innovation)

#count supplychain
count_supplychain=supplychain(text)
print(count_supplychain)
#count governanceparties
count_governanceparties=governanceparties(text)
print(count_governanceparties)
#count riskfactors
count_riskfactors=riskfactors(text)
print(count_riskfactors)
#count governmentcontracting
count_governmentcontracting=governmentcontracting(text)
print(count_governmentcontracting)
#count riskcontrols
count_riskcontrol=riskcontrol(text)
print(count_riskcontrol)
#count thirdparty
count_thirdparty=thirdparty(text)
print(count_thirdparty)
#count personnelatrisk
count_personatrisk=personatrisk(text)
print(count_personatrisk)
# Count healthcare 
count_healthcare = count_healthcare(text)
print(count_healthcare)
# Count intergovernancehelp
count_igh = igh(text)
print( count_igh)
# Count investigativesystems
count_investigativesystems = investigativesystem(text)
print( count_investigativesystems)
# Count Board and CEO
count_board = board(text)
print(count_board)
# Count Strategy
count_strategy = strategy(text)
print(count_strategy)
# Count culture
count_culture = culture(text)
print(count_culture)

# Count Information System
count_info = info(text)
print( count_info)
# Count Fraud
count_fraud = fraud(text)
print(count_fraud)
file.close()






