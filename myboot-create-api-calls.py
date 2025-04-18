from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

TOKEN = '7926957867:AAEqoVnKPlFhDlX_Yjop_smD9x86zdhyeXo'


def start(update, context):
    update.message.reply_text("Hi! I'm your bot.")


def echo(update, context):
    update.message.reply_text(f"You said: {update.message.text}")


def help(update, context):
    update.message.reply_text(
        f"1. For a list of git owner repositories use '/get_repos' flowing Git owne's name.\n"
        f"2. For top 10 repositories in GitHub use /get_top_10_repos.\n"
        f"3. For a list of GitHub branches, use /get_branches flowing owner and repo name.\n"
        f"4. TBD"
    )

# Exercise 1: Get the repositores of a user in github via api calls to github api


def get_repos(update, context):
    try:
        args = context.args
        print(args[0])
        response = requests.get(
            f"https://api.github.com/users/{args[0]}/repos")
        repos = response.json()
        print(response.status_code)
        # update.message.reply_text(f"You sent: {repos[0]['name']}")
        list_repos = []
        for repo in repos:
            list_repos.append(repo['name'])
        # print(list_repos)
        str_repos = '# ' + '\n# '.join(list_repos)
        update.message.reply_text(
            f'List of {args[0]} repositories: \n{str_repos}')
    except Exception as e:
        update.message.reply_text(
            "Check the data you entered and try again.")
        print(e)

# 2. Add a command to get the top 10 repositores in github via api calls to github api


def get_top_10_repos(update, context):
    # TODO: Get the top 10 repositores in github via api calls to github api
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "stars:>0",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }

    response = requests.get(url, params=params)
    data = response.json()
    # print(data.keys())
    # print(type(data['items']))
    list_repos = []
    for i, x in enumerate(data['items'], 1):
        list_repos.append(f"{i}. {x['full_name']}, {x['stargazers_count']}")
    str_repos = ' \n'.join(list_repos)
    update.message.reply_text(f'Top 10 repositores in github:\n{str_repos}')

# 3. Add a commad to get how many branches a repo has via api calls to github api

# owner='non', repo_name='non'


def get_branches(update, context):
    args = context.args

    try:
        owner = args[0]
        repo_name = args[1]
        print(owner)
        print(repo_name)
        # owner = input("Enter owner name: ")
        # repo_name = input("Enter repo name: ")
        url = f"https://api.github.com/repos/{owner}/{repo_name}/branches"
        response = requests.get(url)
        data = response.json()
        status = response.status_code
        print(status)

        if status == 200:
            list_count = []
            for i in data:
                list_count.append(i['name'])
            str_branches = ', '.join(list_count)

            update.message.reply_text(
                f'Owner {owner} in {repo_name} repo, has {len(list_count)} branches.\nBranches list name: {str_branches}.')
        else:
            update.message.reply_text(
                "Check the data you entered and try again.\n{OWNER-NAME} {REPO-NAME}.")
    except Exception as e:
        update.message.reply_text(
            "Check the data you entered and try again.\n{OWNER-NAME} {REPO-NAME}.")
        print(e)

# 4. Check if a GitHub repo has open issues and how many.


def get_open_issues(update, context, repo_name):
    # TODO: Get how many open issues a repo has via api calls to github api
    pass

# 5. Check if a GitHub repo has open pull requests and how many.


def get_open_pull_requests(update, context, repo_name):
    # TODO: Get how many open pull requests a repo has via api calls to github api
    pass

# 6. Add a /weather <city> command→ Use OpenWeatherMap API to return current weather.


def get_weather(update, context, city):
    # TODO: Get the weather of a city via api calls to OpenWeatherMap API
    pass

# 7. Add a /joke command → Use https://official-joke-api.appspot.com/random_joke API to return a random joke.


def get_joke(update, context):
    # TODO: Get a random joke via api calls to https://official-joke-api.appspot.com/random_joke API
    pass


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("get_repos", get_repos))
    dp.add_handler(CommandHandler("get_top_10_repos", get_top_10_repos))
    dp.add_handler(CommandHandler("get_branches", get_branches))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
