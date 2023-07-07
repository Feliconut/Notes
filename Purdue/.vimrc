" Vim with all enhancements
"source $VIMRUNTIME/vimrc_example.vim

""""""""""""""""""
" BASIC EDITOR CUSTOMIZATIONS
""""""""""""""""""

set encoding=utf-8
set fileencoding=utf-8
set ttyfast
set laststatus=2
syntax enable

filetype plugin indent on
set number
"set number relativenumber
" Auto toggle of line numbers https://jeffkreeftmeijer.com/vim-number/
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave,WinEnter * if &nu && mode() != "i" | set rnu   | endif
  autocmd BufLeave,FocusLost,InsertEnter,WinLeave   * if &nu                  | set nornu | endif
augroup END

set hidden
set nocp

set t_Co=256
set cursorline
set conceallevel=2

""""""""""""""""""""""""""
" SETTING UP PLUGINS
""""""""""""""""""""""""""

set rtp+=/opt/homebrew/opt/fzf

call plug#begin('~/.vim/plugged')
Plug 'tpope/vim-surround'

Plug 'junegunn/fzf.vim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }

Plug 'sirver/ultisnips'
let g:UltiSnipsExpandTrigger = '<tab>'
let g:UltiSnipsJumpForwardTrigger = '<tab>'
let g:UltiSnipsJumpBackwardTrigger = '<s-tab>'

Plug 'lervag/vimtex'
filetype plugin indent on
let g:tex_flavor='latex'
let g:vimtex_view_method='skim'
let g:vimtex_quickfix_mode=0
let g:tex_conceal='abdmg'
let g:vimtex_complete_enabled=1
"let g:vimtex_fold_enabled=1

Plug 'sonph/onehalf', { 'rtp': 'vim' }
"Plug 'dylanaraps/wal.vim'

Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
call plug#end()

" C-l in insert mode will auto fix spell error
"set spell spelllang=en_us
"inoremap <C-l> <c-g>u<Esc>[s1z=`]a<c-g>u

" :grep
set grepprg=rg\ --vimgrep\ --smart-case\ --follow

" \lt opens fzf
nnoremap <localleader>lt :call vimtex#fzf#run()<cr>


colorscheme onehalflight

" Shorten the begin and end statements
call matchadd('Conceal', '\\begin{[^}]\+}',    10, -1, {'conceal':'-'})
call matchadd('Conceal', '\\end{[^}]\+}',    10, -1, {'conceal':'-'})
"hi clear Conceal

""""""""""""""""""
" Inkscape Sync Scripts
""""""""""""""""""

inoremap <C-f> <Esc>: silent exec '.!inkscape-figures create "'.getline('.').'" "'.b:vimtex.root.'/figures/"'<CR><CR>:w<CR>
nnoremap <C-f> : silent exec '!inkscape-figures edit "'.b:vimtex.root.'/figures/" > /dev/null 2>&1'<CR><CR>:w<CR>
silent !find -L ~/univ/current_semester -type d | grep "figures$" > .config/inkscape-figures/roots 
silent !inkscape-figures watch
