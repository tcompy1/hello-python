# Toolbox 🧰

A small but growing set of everyday CLI utilities, written in Python, test-driven from the ground up.

## Features

### ✅ Todo manager
Manage simple todos stored locally.

```bash
# add a new todo
toolbox todo add "Read docs"

# list open todos
toolbox todo list

# list all (including done)
toolbox todo list --all

# mark a todo as done
toolbox todo done 1

# remove a todo (asks for confirm unless -y given)
toolbox todo rm 1
toolbox todo rm -y 1
