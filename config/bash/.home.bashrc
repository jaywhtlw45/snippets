# Source my custom bashrc from repo
if [[ -f "$HOME/code/snippets/config/bash/.bashrc" ]]; then
    source "$HOME/code/snippets/config/bash/.bashrc"
    echo "Sourced bashrc"
elif [[ -f "$HOME/snippets/config/bash/.bashrc" ]]; then
    source "$HOME/snippets/config/bash/.bashrc"
    echo "Sourced bashrc"
else
    echo "Could not source bashrc"
fi