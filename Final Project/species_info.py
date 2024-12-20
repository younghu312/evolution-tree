from base64 import b64encode

def get_encoded_image(image_path):
    with open(image_path, 'rb') as image_file:
        encoded = b64encode(image_file.read()).decode()
    return f'data:image/jpeg;base64,{encoded}'

# Species information dictionary
species_info = {
    "Homo sapiens": {
        "common_name": "Modern Human",
        "description": "Homo sapiens, the species to which all modern humans belong, is the only surviving member of the genus Homo. This species is characterized by a large brain, upright posture, and bipedal locomotion. Homo sapiens first appeared in Africa over 315,000 years ago and later spread across the globe, replacing or interbreeding with other hominin species such as Neanderthals. They are distinguished by their ability to create complex tools, use language, and develop cultures. The species exhibits significant genetic diversity, yet the differences among global populations are minor compared to the variation within each population.",
        "distribution": "Worldwide",
        "features": "Large brain (1300-1400cc), bipedal locomotion, complex language capabilities",
        "image_url": get_encoded_image("images/homo_sapiens.png")
    },
        "Homo sp. (Denisovan)": {
        "common_name": "Denisovans",
        "description": "Denisovans were an archaic human group that lived in Asia and are known from fossils found in Siberia and other parts of Asia. They interbred with Neanderthals and early modern humans, leaving genetic traces in some modern populations, especially in Oceania.",
        "distribution": "Eastern and Southern Asia, parts of Melanesia, possibly as far as the Philippines and New Guinea",
        "features": "Genetically distinct from Neanderthals and modern humans, with significant genetic contributions to some modern populations, particularly in Oceania",
        "image_url": get_encoded_image("images/denisovan.png")
    },
    "Homo neanderthalensis": {
        "common_name": "Neanderthal",
        "description": "Neanderthals, were a group of archaic humans who lived in Eurasia from at least 200,000 years ago until they were replaced or assimilated by early modern humans between 35,000 and 24,000 years ago. They were adapted to cold climates, with a robust build, short limbs, and a broad chest. Neanderthals had distinctive cranial features, including a low-vaulted cranium, large brow ridges, and a pronounced occipital region. They developed a complex culture, using advanced stone tools and engaging in symbolic behaviors such as burial rituals. Genetic evidence shows that Neanderthals interbred with modern humans, contributing to the gene pool of non-African populations.",
        "distribution": "From the Atlantic regions of Europe eastward to Central Asia, reaching as far north as present-day Belgium and as far south as the Mediterranean and southwest Asia",
        "features": "Stocky, cold-adapted build, Prominent cranial and dental features, Complex social behavior",
        "image_url": get_encoded_image("images/neandethal.png")
    },
    "Pan paniscus": {
        "common_name": "Bonobo",
        "description": "Bonobos are similar in appearance to chimpanzees but are more slender, with longer limbs and a rounder head. They primarily feed on fruits and vegetation, occasionally consuming invertebrates. Unlike chimpanzees, bonobos do not hunt monkeys and exhibit more peaceful social behaviors, with less aggression and no observed infanticide or cannibalism. Bonobos live in communities of 30 to over 100 individuals, with females playing a central role in social structures. They are endangered due to habitat destruction and illegal hunting, with populations declining to around 20,000 by 2016.",
        "distribution": "Democratic Republic of the Congo",
        "features": "Matriarchal society, slender than chimpanzees, highly social behavior",
        "image_url": get_encoded_image("images/bonobo.png")
    },
    "Pan troglodytes": {
        "common_name": "Common Chimpanzee",
        "description": "Chimpanzees (Pan troglodytes) are a species of ape closely related to humans, inhabiting the tropical forests and savannas of equatorial Africa. They stand about 1 to 1.7 meters tall and weigh between 32 to 60 kilograms, with males generally larger than females. Covered in brown or black hair, their faces are bare except for a short white beard, and their skin is mostly white, except for black faces, hands, and feet. Chimpanzees are highly social, living in communities with complex social structures and behaviors, including cooperation, grooming, and forming alliances. They are primarily vegetarian but also hunt and use tools. Chimpanzees are endangered due to hunting, habitat destruction, and other threats.",
        "distribution": "Tropical forests and savannas of equatorial Africa",
        "features": "Tool use, complex social structures, omnivorous diet",
        "image_url": get_encoded_image("images/chimp.png")
    },
    "Gorilla gorilla": {
        "common_name": "Gorilla",
        "description": "Gorillas are robust and powerful, with black skin and hair, and adult males, known as silverbacks, have a distinctive gray or silver saddle on their backs. They live in stable family groups led by one or more silverbacks and are primarily terrestrial, using knuckle walking for locomotion. Gorillas are mainly vegetarian, feeding on leaves, stems, and fruits, and are known for their gentle and shy nature unless threatened. Unfortunately, all gorilla species are critically endangered due to habitat destruction and poaching.",
        "distribution": "Tropical forests of equatorial Africa",
        "features": "Pronounced sexual dimorphism, herbivorous diet, knuckle-walking",
        "image_url": get_encoded_image("images/gorilla.png")
    },
    "Pongo abelii": {
        "common_name": "Sumatran Orangutan",
        "description": "The Sumatran orangutan (Pongo abelii) is a critically endangered species of great ape found exclusively in the rainforests of northern Sumatra. Known for their distinctive reddish-brown hair, Sumatran orangutans are highly intelligent, possessing cognitive abilities similar to those of gorillas and chimpanzees. Their population is estimated to be around 13,800 individuals, and they face significant threats from habitat loss due to deforestation for agriculture, particularly palm oil plantations, as well as poaching. Conservation efforts are crucial to prevent their extinction, as their numbers continue to decline due to these ongoing threats.",
        "distribution": "Northern Sumatra, Indonesia",
        "features": "Semi-solitary, Arboreal Lifestyle, distinctive red fur",
        "image_url": get_encoded_image("images/sumatran.png")
    },
    "Pongo pygmaeus": {
        "common_name": "Bornean Orangutan",
        "description": "The Bornean orangutan (Pongo pygmaeus) is a critically endangered species native to the island of Borneo. These great apes are characterized by their reddish-brown hair and large, robust bodies. Males are distinguished by their prominent cheek pads and throat pouches, which are used for vocalizations. Bornean orangutans are primarily arboreal, spending much of their time in the trees of tropical rainforests. Their population has significantly declined due to habitat destruction from logging, agricultural expansion, particularly palm oil plantations, and hunting. Conservation efforts are crucial to prevent further population decline, as their numbers have decreased by more than 50% since the 1970s.",
        "distribution": "Island of Borneo in Southeast Asia",
        "features": "Primarily frugivorous, Arboreal Lifestyle, Known for their cognitive abilities",
        "image_url": get_encoded_image("images/bornean.png")
    },
    "Hylobates agilis": {
        "common_name": "Agile Gibbon",
        "description": "The Agile gibbon, or the black-handed gibbon, is a species of small ape found in the tropical forests of Southeast Asia, specifically on Sumatra south of Lake Toba and on the Malay Peninsula between the Perak and Mudah rivers. This gibbon can be either tan or black and is distinguished by its white facial markings. Like other gibbons, Hylobates agilis is arboreal and moves with remarkable agility through the trees by brachiation, swinging from branch to branch using its long arms. Gibbons are known for their loud, musical vocalizations, which serve as territorial markers. They live in small monogamous groups and primarily feed on fruit, with some leaves, insects, and bird eggs included in their diet.",
        "distribution": "Tropical forests of Southeast Asia",
        "features": "Highly agile, monogamous pairs, complex vocalizations",
        "image_url": get_encoded_image("images/agilegibbon.jpg")
    },
    "Hylobates lar": {
        "common_name": "White-handed Gibbon",
        "description": "The white-handed gibbon is a small ape found in northern Sumatra, the Malay Peninsula, Thailand, and Yunnan, China. It is part of the genus Hylobates, known for being the smallest gibbons with the densest body hair. The white-handed gibbon is characterized by its white extremities, contrasting with its otherwise tan or black fur. These gibbons are arboreal, moving swiftly through trees by brachiation, and are known for their loud, musical vocalizations used for communication and territorial marking. They live in small monogamous groups, primarily feeding on fruit, with some leaves, insects, and bird eggs. Like other gibbons, they are increasingly threatened by habitat destruction and are considered endangered.",
        "distribution": "Southeast Asia and China",
        "features": "Among the smallest gibbons with the densest body hairs, remarkable brachiation",
        "image_url": get_encoded_image("images/whitehanded.png")
    },
    "Hylobates pileatus": {
        "common_name": "Pileated Gibbon",
        "description": "The pileated gibbon is a species found in southeastern Thailand and western Cambodia. It is characterized by its distinctive coloration: males are black, while females are buff with a black cap and chest patch. Both sexes have white hands and feet. Juveniles are initially buff, and both sexes darken with age, with males doing so more rapidly. Like other gibbons, pileated gibbons are arboreal and known for their agility in swinging from branch to branch. They live in small monogamous groups and are primarily frugivorous, feeding on fruits, leaves, and occasionally insects and bird eggs.",
        "distribution": "Thailand, Cambodia, Laos",
        "features": "Sexual dichromatism, complex songs, territorial behavior",
        "image_url": get_encoded_image("images/pileated.png")
    },
    "Symphalangus syndactylus": {
        "common_name": "Siamang",
        "description": " Siamang is an arboreal ape belonging to the gibbon family (Hylobatidae). It is native to the forests of Sumatra and the Malay Peninsula. The siamang is distinguished by its robust build, completely black shaggy fur, and a unique webbing between its second and third toes. It also has a large, hairless throat sac that can be inflated to produce a resonant, booming call. Siamangs are about 50–55 centimeters in body length and are the largest of the gibbons, with males weighing around 12 kg and females about 10.5 kg. They are diurnal and arboreal, moving primarily by brachiation, and their diet mainly consists of fruit. Siamangs typically live alone or in small groups, and their gestation period is about 230 days, usually resulting in a single offspring. They are the sole members of the genus Symphalangus.",
        "distribution": "Forests of Sumatra and the Malay Peninsula",
        "features": "Throat sac for calls, larger than other gibbons, webbed toes",
        "image_url": get_encoded_image("images/siamang.png")
    },
    "Nomascus siki": {
        "common_name": "Southern White-cheeked Gibbon",
        "description": "The Southern White-cheeked Gibbon is a species of gibbon found in Southeast Asia. These gibbons are characterized by their distinctive vocalizations, which are used for communication and territorial marking. In the Nomascus genus, both sexes are black as juveniles, but females lighten to a buff color as they mature, resulting in distinct adult appearances between the sexes. The Southern White-cheeked Gibbon is closely related to the Northern White-cheeked Gibbon (Nomascus leucogenys) and is found further south in its range. Like other gibbons, they are arboreal, moving through the trees with agility by brachiating, and they live in small, monogamous family groups. Gibbons are among the most endangered primates due to habitat destruction and hunting pressures.",
        "distribution": "Southeast Asia",
        "features": "Sexual dimorphism in coloration, complex vocal repertoire",
        "image_url": get_encoded_image("images/southern.png")
    }
}
