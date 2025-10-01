# Source my custom bashrc from repo
REPO_PATH="$HOME/snippets"

if [[ -d "$REPO_PATH" ]]; then
    # Attempt to pull latest changes
    echo "Updating repo at $REPO_PATH..."
    (cd "$REPO_PATH" && git pull --quiet 2>/dev/null)
    
    # Source the bashrc if it exists
    BASHRC_PATH="$REPO_PATH/config/bash/.bashrc"
    if [[ -f "$BASHRC_PATH" ]]; then
        source "$BASHRC_PATH"
        echo "Sourced bashrc from $BASHRC_PATH"
    else
        echo "Could not source bashrc"
    fi
else
    echo "Repository not found at $REPO_PATH"
fi  
