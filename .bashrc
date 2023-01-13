# Set the prompt
PS1='\n\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '

# Set the terminal title to the current working directory
PROMPT_COMMAND='echo -ne "\033]0;${PWD##*/}\007"'

# Add the current working directory to the command history
export HISTFILESIZE=10000
export HISTSIZE=10000
export HISTTIMEFORMAT="%F %T "
PROMPT_COMMAND="${PROMPT_COMMAND:+$PROMPT_COMMAND;}history -a; history -n; $PROMPT_COMMAND"

# Show git branch in prompt
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

export PS1="\n\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;33m\]\$(parse_git_branch)\[\033[1;31m\]\$\[\033[0m\] "

# Show time in prompt
export PS1="\n\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;33m\]\$(parse_git_branch)\[\033[1;33m\] \t \[\033[1;31m\]\$\[\033[0m\] "

