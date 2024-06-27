local auto_save_file_group = vim.api.nvim_create_augroup('AutoSavePyFileGroup', { clear = true })
vim.api.nvim_create_autocmd({ 'BufWritePost' }, {
  group = auto_save_file_group,
  pattern = "*.py",
  command = "silent !ruff --fix % | ruff format % | ruff check --fix %"
})
