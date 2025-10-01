# Git branch parsing function
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# Color variables
RED="\[\033[0;31m\]"
GREEN="\[\033[0;32m\]"
BLUE="\[\033[0;34m\]"
YELLOW="\[\033[0;33m\]"
MAGENTA="\[\033[0;35m\]"
CYAN="\[\033[0;36m\]"
WHITE="\[\033[0;37m\]"
NC="\[\033[0m\\]" # No Color

# Customize PS1 with Git branch and colors
export PS1="${GREEN}\u@\h${NC}:${BLUE}\w${NC}${YELLOW}\$(parse_git_branch)${NC}\$ "
