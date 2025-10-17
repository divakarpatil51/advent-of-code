local function select_input_to_run()
  local env_map = {
    [1] = "test",
    [2] = "real",
  }
  Snacks.picker.select({
      "test",
      "real",
    },
    { prompt = "Select input to run" },
    function(item, idx)
      local env = env_map[idx]
      local file_name = vim.fn.expand('%:p')
      local file_extension = file_name:match("^.+(%..+)$")

      local cmd = ":w | split | terminal"
      Snacks.notify.info("Running with " .. env .. " input", { title = "AOC" })
      vim.env["AOC_ENV"] = env
      if file_extension == ".py" then
        vim.cmd(cmd .. " python %")
        return
      end
      if file_extension == ".go" then
        vim.cmd(cmd .. " go run %")
        return
      end
      if file_extension == ".lua" then
        vim.cmd(cmd .. " lua %")
        return
      end
    end
  )
end

vim.keymap.set("n", "<F10>", select_input_to_run, { desc = "Run app" })
