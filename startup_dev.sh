#!/bin/bash

# Create a new Tmux session named "my-project"
tmux new-session -d -s loi-tool

# Split the window horizontally into two panes
tmux split-window -h

# Send the first command to the left pane
tmux send-keys -t 0 "source loi_env/bin/activate; cd backend_flask; python app.py" C-m

# Send the second command to the right pane
#tmux send-keys -t 1 "source loi_env/bin/activate; cd frontend_react_loi-tool; PORT=5000 npm start" C-m
tmux send-keys -t 1 "source loi_env/bin/activate; cd frontend_react_loi-tool; npm start" C-m

# Attach to the session
tmux attach-session -t loi-tool
