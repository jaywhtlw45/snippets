# WSL distro auto-completion for bash
# https://claude.ai/chat/6e7108ee-8311-4f11-8a11-04641f88735a
_wsl_complete() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    
    # Options that expect a distro name
    if [[ "$prev" == "-d" ]] || [[ "$prev" == "--distribution" ]] || \
       [[ "$prev" == "-s" ]] || [[ "$prev" == "--set-default" ]] || \
       [[ "$prev" == "-t" ]] || [[ "$prev" == "--terminate" ]]; then
        # Get list of installed WSL distros
        local distros=$(wsl.exe -l -q 2>/dev/null | tr -d '\r' | sed 's/\x0//g' | grep -v '^$')
        COMPREPLY=( $(compgen -W "$distros" -- "$cur") )
        return 0
    fi
    
    # Complete WSL command options
    opts="-d --distribution -u --user --exec -e --system --shell-type -s --set-default \
          --unmount --mount --shutdown -t --terminate --export --import --set-version \
          -l --list --status --help --version"
    COMPREPLY=( $(compgen -W "$opts" -- "$cur") )
    return 0
}

# Register the completion function
complete -F _wsl_complete wsl
complete -F _wsl_complete wsl.exe
