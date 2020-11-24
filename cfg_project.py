import requests
headers = {'Content-Type': 'application/json'}
apiKey = 'apiKey=8fc48b9af3a349e38ffcbb5ed2ffa3d9'
supplies = input("Which ingredients do you want to cook with tonight? ")
components = supplies.split()
items = ',+'.join(components)
ingredient = 'ingredients=' + items
includeIngredients = "includeIngredients={}".format(supplies)
addRecipeNutrition="addRecipeNutrition=true"
#The basic scenario for recipe retrieval, involving desired ingredients
dietUrl = 'https://api.spoonacular.com/recipes/complexSearch?{}&{}'.format(apiKey, addRecipeNutrition)
#Asking whether they've got any dietary requirements
dietChoice = input("Do you have any dietary requirements - Yes/No? ")
if dietChoice == 'Yes':
    dietRequirement = input("What is your dietary requirement? ")
    diet = "diet={}".format(dietRequirement)
    dietUrl = dietUrl + '&{}'.format(diet)
#Asking whether they're craving a certain cuisine
cuisineChoice = input("Are there any cuisines you're in the mood for - Yes/No? ")
if cuisineChoice == 'Yes':
    cuisinePreferred = input("What is your preferred cuisine? ")
    cuisine = "cuisine={}".format(cuisinePreferred)
    dietUrl = dietUrl + '&{}'.format(cuisine)
#Asking whether they have a time limit to prepare the dish
timeLimit = input("Are you pressed for prep time - Yes/No? ")
if timeLimit == 'Yes':
    timeMins = input("What's the max amount of time you have to make dinner, in minutes? ")
    maxReadyTime = "maxReadyTime={}".format(int(timeMins))
    dietUrl = dietUrl + '&{}'.format(maxReadyTime)
response = requests.get(dietUrl)
dietaryRecipesRaw = response.json()
dietaryRecipes = dietaryRecipesRaw['results']
print('Here are your recipe options that include {}: '.format(items))
for d in range(0, len(dietaryRecipes)):
    print(dietaryRecipes[d]['title'])
    dietaryNutrition = (dietaryRecipes[d]['nutrition'])
    nutrients = (dietaryNutrition['nutrients'])
    print(nutrients[0]['amount'])
    print(nutrients[0]['unit'] + " per serving")