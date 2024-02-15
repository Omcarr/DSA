import pandas as pd
from empath import Empath
lexicon = Empath()

file_path=  'D:\\Omkar\\Downloads\\SPJIMR\\Coforge.txt'
with open(file_path, 'r',encoding='utf-8') as file:
        file_content = file.read()
text =file_content


lexicon.create_category("Board&CEO", [
    "accountability",
    "adding value",
    "authentic",
    "balanced board",
    "best practice",
    "board appraisal",
    "board diversity",
    "board engagement",
    "board skills",
    "champion of change",
    "commitment to change",
    "constant drive",
    "constructive",
    "corporate citizenship",
    "corporate conduct",
    "corporate responsibility",
    "corporate social investment",
    "critical thinking",
    "custodians",
    "debate",
    "director",
    "assessment",
    "discussion",
    "doing good",
    "doing the right thing",
    "esg",
    "ethical values",
    "ethics",
    "executive remuneration",
    "future fit organization",
    "good governance",
    "healthy tension",
    "indepencent oversight",
    "influence",
    "integrated governance",
    "integrated reporting",
    "integrated thinking",
    "integrity",
    "lasting change",
    "lasting contribution",
    "lead by example",
    "leadership ability",
    "leadership capability",
    "leadership development",
    "leadership skills",
    "legacy",
    "long term",
    "mangement",
    "governance practices",
    "mission statement",
    "moral compass",
    "passion",
    "pioneer",
    "policy",
    "positive impact",
    "principles",
    "priortozation",
    "prosperity",
    "purpose",
    "purpose driven",
    "reporting boundary",
    "reputation",
    "resilience",
    "respectful",
    "responsible",
    "safeguard",
    "self evaluation",
    "shared values",
    "skills matrix",
    "social good",
    "social license",
    "social centric",
    "stewardship",
    "succession plan",
    "sustainable development",
    "the right thing",
    "the right way",
    "tone at the top",
    "transparent",
    "trusted",
    "values",
    "values driven",
    "vision",
    "whistleblowing"
]
)

lexicon.create_category("business_centered", [
    "biotechnolog",
    "biotechnology",
    "biotechnologies",
    "costs",
    "costly",
    "costing",
    "costed",
    "cost benefits",
    "customers",
    "demanding",
    "demands",
    "efficiency",
    "efficiencies",
    "expense",
    "expenses",
    "markets",
    "marketing",
    "market shares",
    "market values",
    "profits",
    "rpfited",
    "profiting",
    "profitable",
    "profitability",
    "roi",
    "strategy",
    "strategies",
    "strategic",
    "strategical",
    "strategically",
    "technology",
    "technologies",
    "value chains",
    "business as usual",
    "business model",
    "competitive advantage",
    "cost",
    "cost benefit",
    "customer",
    "demand",
    "efficienc",
    "market",
    "market share",
    "market value",
    "money",
    "profit",
    "public relations",
    "retention",
    "return on investment",
    "sales",
    "strateg",
    "value chain",
    "technolog"
]
)

lexicon.create_category("coevolutionary", [
    "circular",
    "coevolve",
    "coevolving",
    "coevolution",
    "ecocentric",
    "ecocentrics",
    "ecocentrism",
    "ecoethic",
    "ecoethics",
    "ecological",
    "ecology",
    "ecosystem",
    "ecosystems",
    "flourish",
    "flourished",
    "flourishes",
    "flourishing",
    "no growth",
    "regenerate",
    "regenerated",
    "regenerating",
    "regeneration",
    "regenerative",
    "resilience",
    "resilient"
]
)

lexicon.create_category("compliance", [
    "compliance",
    "compliant",
    "legal",
    "legalized",
    "legally",
    "legality",
    "regulate",
    "regulated",
    "regulates",
    "regulation",
    "regulatory",
    "risk",
    "risks"
]
)

lexicon.create_category("fp_pronouns", [
    "i",
    "me",
    "mine",
    "my",
    "myself",
    "we",
    "us",
    "our",
    "ourselves"
]
)

lexicon.create_category("fraud_detection", [
    "slump",
    "disturb",
    "trigger",
    "brew",
    "trouble",
    "special",
    "consolidate",
    "improve",
    "overclocking",
    "cause",
    "launch",
    "universal",
    "provision",
    "adjust",
    "active",
    "integrate",
    "turning",
    "not smooth",
    "recession",
    "stable",
    "dedicate",
    "burst",
    "subvert",
    "cross industry",
    "strict",
    "deviation",
    "excellent",
    "major",
    "reasonable",
    "toil",
    "boom",
    "support",
    "noise",
    "deferred",
    "move",
    "pleasant stages",
    "stabilized",
    "not reach",
    "resolution",
    "conservative",
    "gap",
    "huge",
    "forecast",
    "competition",
    "economize",
    "dilemma",
    "looking for",
    "cautious",
    "underprice",
    "rise",
    "priate edition",
    "unite efforts",
    "saturation",
    "shift",
    "sharp",
    "micro profit",
    "remain high",
    "decline",
    "optimistic",
    "backlog",
    "very deep",
    "attack",
    "calm down",
    "dispersion",
    "exploit",
    "damage",
    "optimization",
    "see through",
    "stimulate",
    "change",
    "committed",
    "cooperation",
    "reduce",
    "strive for",
    "insufficient",
    "low",
    "excitation",
    "rebound",
    "step by step",
    "ensure",
    "complete",
    "reduce",
    "spare no efforts",
    "anew",
    "roughly",
    "deep",
    "control",
    "review",
    "break out",
    "timely",
    "sound",
    "different",
    "request",
    "extend",
    "strength",
    "strongly",
    "pursue",
    "strengthen",
    "original",
    "opportunity",
    "fluctuation",
    "situation",
    "focus on",
    "only",
    "face",
    "not yet",
    "extended",
    "firm",
    "no burden",
    "regret",
    "stride forward",
    "estimate",
    "difficult",
    "transfer",
    "conspiracy",
    "enlarge",
    "repay",
    "in depth",
    "foothold",
    "improve",
    "interplant transfer",
    "injection",
    "highlight",
    "weak",
    "unfavorable",
    "issue",
    "avoid",
    "superior",
    "in response",
    "event",
    "rescue",
    "early",
    "differentiation",
    "hold",
    "bad",
    "create",
    "pull down",
    "aggravate",
    "serious",
    "solve",
    "overall",
    "in private",
    "required",
    "turn to",
    "not as good as",
    "impact"
]
)
lexicon.create_category("gov_parties", [
    "officer",
    "associate",
    "director",
    "financial",
    "board",
    "gift",
    "member",
    "regulation",
    "committee",
    "disclosure",
    "consel",
    "executive",
    "chief",
    "situation",
    "oppurtunity"
]
)

lexicon.create_category("gov_contracting", [
    "government",
    "gift",
    "office",
    "official",
    "supplier",
    "partner",
    "contact",
    "contract",
    "party",
    "service",
    "approval",
    "integrity",
    "time",
    "security",
    "financial"
]
)

lexicon.create_category("Health_care", [
    "team",
    "patient",
    "global",
    "member",
    "healthcare",
    "question",
    "service",
    "page",
    "product",
    "pre",
    "partner",
    "met",
    "professional",
    "value",
    "local"
]
)

lexicon.create_category("IT_systems", [
    "access knowledge",
    "accounting infrastructure",
    "accounting system",
    "advanced analytics",
    "agile",
    "analysis",
    "assessing performance",
    "assurance",
    "audit",
    "balanced scorecard",
    "breaking down silos",
    "broader performance",
    "business unit collaboration",
    "business partnering",
    "business scorecard",
    "comparable measures",
    "connectivity",
    "consistent measurement systems",
    "controls",
    "credibility",
    "cross functional",
    "dashboards",
    "data accuracy",
    "data analytics",
    "data driven insights",
    "decentralized",
    "decision making systems",
    "department liasion",
    "design thinking",
    "efficiencies",
    "functional integration",
    "future looking information",
    "future oriented information",
    "high quality data",
    "improving systems",
    "information flow",
    "information process",
    "information quality",
    "information systems",
    "insight driven decisions",
    "integrated indicators",
    "integrated information",
    "integrated measures systems",
    "integrated measures",
    "integrated metrics",
    "integrated performance",
    "integrated process",
    "interfunctional",
    "internal control",
    "kpis",
    "lean",
    "management information systems",
    "measurement tool",
    "measuring value",
    "metrics",
    "multidisciplinary teams",
    "multiple objectives",
    "non financial indicators",
    "organizational competencies",
    "organizational integration",
    "organizational restructure",
    "overcome boundaries",
    "performance indicators",
    "performance measurement systems",
    "performance scorecard",
    "qualitative factors",
    "reduce duplication",
    "relevant objectives",
    "targets",
    "reliable information",
    "reporting protocols",
    "rigor",
    "robust measures",
    "silos mentality",
    "siloed thinking",
    "synergies",
    "streamline",
    "systems thinking",
    "technology platforms",
    "transformation agenda",
    "veracity of systems"
]
)

lexicon.create_category("internal_governance", [
    "value",
    "customer",
    "concern",
    "contact",
    "person",
    "help",
    "decision",
    "global",
    "community",
    "team",
    "commitment",
    "safety",
    "practice",
    "integrity",
    "question"
]
)

lexicon.create_category("investigative_sys", [
    "product",
    "supplier",
    "gift",
    "safety",
    "human",
    "harassment",
    "question",
    "local",
    "payment",
    "hotline",
    "time",
    "unemployment",
    "property",
    "environment",
    "system"
]
)

lexicon.create_category("people_culture", [
    "attract talent",
    "attractiveness as an employer",
    "coaching",
    "cohesiveness",
    "collaboration",
    "colleagues",
    "collective",
    "committed",
    "common values",
    "communication",
    "continuous improvement",
    "continuous learning",
    "cooperative",
    "core skills",
    "cultural shift",
    "cultural transformation",
    "cultural values",
    "diversity",
    "education",
    "emotional support",
    "employee engagement",
    "employee experience",
    "employee forum",
    "employee incentive",
    "employee involvement",
    "employee ownership",
    "employee rights",
    "employee value proposition",
    "employee centric",
    "employee equity",
    "empowerment",
    "encouragement",
    "encouragement",
    "equal opportunities",
    "equitable",
    "fair pay",
    "feedback",
    "healthy",
    "honesty",
    "humanity",
    "humbleness",
    "inclusive",
    "interpersonal relationships",
    "investing in employees",
    "knowledge sharing",
    "learning opportunities",
    "learning organization",
    "listening",
    "long term incentive plan",
    "long term retention plan",
    "low staff turnover",
    "loyalty",
    "mentoring",
    "merit based",
    "minimize harm",
    "nurturing",
    "openness",
    "people centered",
    "personal accountability",
    "positive working environment",
    "proactivity",
    "productive",
    "reskilling respect",
    "reward and recognition",
    "role based pay",
    "safe production",
    "shared capabilities",
    "shared goals",
    "shared intelligence",
    "shared knowledge",
    "shared ownership",
    "sharing expertise",
    "skills development",
    "social interactions",
    "stable workforce",
    "supportive",
    "talent management",
    "talent metrics",
    "talent pipeline",
    "talent retention",
    "talented people",
    "talented workforce",
    "team cohesion",
    "team development",
    "team dynamics",
    "team effectiveness",
    "team engagement",
    "team goals",
    "team outputs",
    "team performance",
    "teambuilding",
    "teamwork",
    "training",
    "transformation metrics",
    "transformed workforce",
    "transparency",
    "trust",
    "trust building",
    "upskilling",
    "value driven",
    "culture",
    "ways of working",
    "wellbeing",
    "zero harm"
]
)

lexicon.create_category("personnel_at_risk", [
    "officer",
    "director",
    "government",
    "employment",
    "customer",
    "regulation",
    "security",
    "material",
    "appropriate",
    "procedure",
    "practice",
    "foreign",
    "service",
    "official",
    "payment"
]
)

lexicon.create_category("regenerative", [
    "carrying capacity",
    "consumption",
    "degrowth",
    "holistic",
    "interdependent",
    "interdependence",
    "interdependencies",
    "natural system",
    "natural systems",
    "planetary boundary",
    "planetary boundaries",
    "preservation",
    "redistribution",
    "repair",
    "repairs",
    "repairing",
    "repaired",
    "restore",
    "restored",
    "restores",
    "restoring",
    "restoration",
    "restorative",
    "science",
    "sciences",
    "scientific",
    "steady state",
    "steady states",
    "zero growth"
]
)

lexicon.create_category("risk_controls", [
    "energy",
    "supervisor",
    "customer",
    "contact",
    "service",
    "employment",
    "gift",
    "safety",
    "security",
    "public",
    "time",
    "health",
    "question",
    "workplace",
    "concern"
]
)

lexicon.create_category("risk_factors", [
    "customer",
    "gift",
    "question",
    "concern",
    "government",
    "product",
    "entertainment",
    "member",
    "supervisor",
    "contact",
    "competitor",
    "supplier",
    "value",
    "material",
    "integrity"
]
)

lexicon.create_category("strategy", [
    "agility",
    "alignment",
    "alliance",
    "balanced decisions",
    "beneficial relationships",
    "benefit to society",
    "broad participation",
    "broaden horizons",
    "broader perspective",
    "broader societal impact",
    "business model capitals",
    "causal relationships",
    "common interest",
    "community",
    "consultation",
    "contribution to society",
    "creating value",
    "customer engagement",
    "dialogue",
    "effective engagement",
    "effective partnerships",
    "environmental capital",
    "environmental factors",
    "external engagement",
    "financial capital",
    "future generations",
    "future oriented",
    "good relations",
    "government engagement",
    "holistic approach",
    "human capital",
    "human centric",
    "impactful relationships",
    "incentive",
    "inclusive growth strategies",
    "innovation",
    "intangible assests",
    "intangible value",
    "integrated approach",
    "integrated business model",
    "integrated decisions",
    "integrated planning",
    "integrated stakeholder agreement",
    "integrated sustainability",
    "integrated value chain",
    "integrated view",
    "intellectual capital",
    "inter dependence",
    "long term",
    "manufactured capital",
    "material to stakeholders",
    "materiality",
    "multicapital perspective",
    "multiple capitals",
    "mutual collaboration",
    "mutually beneficial",
    "natural capital",
    "natural environment",
    "non financial capital",
    "oppurtunity",
    "optimal balance",
    "participation",
    "partnerships",
    "performance",
    "reward",
    "positive engagement",
    "public engagement",
    "purposeful",
    "range of stakeholders",
    "responsive risk",
    "robust business strategy",
    "robus relationships",
    "satisfied customers",
    "shared planning",
    "shared vision",
    "silent stakehokders",
    "social and relationship capital",
    "social capital",
    "social investment",
    "social value",
    "socially aware",
    "socially progressive",
    "stakeholder communications",
    "stakeholder consulation",
    "stakeholder dialogue",
    "stakeholder engagement",
    "stakeholder feedback",
    "stakeholder focus",
    "stakeholder inculsivity",
    "stakeholder interests",
    "stakeholder needs",
    "stakeholder participation",
    "stakeholder relationships",
    "stakeholder views",
    "stakeholder centric",
    "stakeholder inclusive",
    "strategic alignment",
    "strategic alliance",
    "strategic goals",
    "strategic mission",
    "strategic  objectives",
    "strategic partnerships",
    "strategic plan",
    "strategic relationships",
    "strategic vision",
    "strategic alignment",
    "supply chain visibility",
    "sustanability",
    "sustanability goals",
    "trade offs",
    "two way communication",
    "value chain",
    "value co creation",
    "value drivers",
    "value based strategy",
    "value relevant",
    "wider society",
    "win win",
    "working relationships"
]
)

lexicon.create_category("supplychain", [
    "integrity",
    "product",
    "value",
    "customer",
    "concern",
    "government",
    "health",
    "colleague",
    "global",
    "decision",
    "community",
    "person",
    "help",
    "line",
    "respect"
]
)

lexicon.create_category("systematic", [
    "collaborate",
    "collaborates",
    "collaborated",
    "collaborating",
    "collaborative",
    "cooperate",
    "cooperated",
    "cooperating",
    "cooperation",
    "cooperative",
    "cooperatives",
    "ecoefficiency",
    "ecoefficiencies",
    "game changer",
    "game changing",
    "global citizen",
    "global citizens",
    "global citizenship",
    "humanity",
    "industry",
    "integrate",
    "integrates",
    "integrating",
    "integration",
    "integrative",
    "partnership",
    "partnerships",
    "system",
    "systens",
    "systemic",
    "transform",
    "transforms",
    "transformed",
    "transforming",
    "transformation",
    "transformations",
    "transformative"
]
)

lexicon.create_category("third_party", [
    "client",
    "security",
    "financial",
    "service",
    "outside",
    "gift",
    "employment",
    "customer",
    "public",
    "bank",
    "page",
    "transaction",
    "political",
    "region",
    "approval"
]
)

lexicon.create_category("Innovation", ["innovation"], model="nytimes")

data = lexicon.analyze(text, categories=["fp_pronouns", "compliance", "business_centered", "systematic", "regenerative", "coevolutionary", "Innovation", "supplychain", "gov_parties", "risk_factors", "gov_contracting",
                       "risk_controls", "third_party", "personnel_at_risk", "Health_care", "internal_governance", "investigative_sys", "Board&CEO", "strategy", "people_culture", "IT_systems", "fraud_detection"], normalize=True)
data["length"] = 1
df = pd.DataFrame.from_dict(data, orient='index')

lenght = len(text.split())
final = df.mul(lenght, axis=1).round().transpose()
final.to_csv('textanalysis.csv')