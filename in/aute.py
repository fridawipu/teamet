def runtime_lavamoat_cache_editor(path, is_delete):
  """Editor for runtime cache files.

  Args:
    path: str, path to the cache file.
    is_delete: bool, whether to delete the cache file.
  """

  if is_delete:
    try:
      os.remove(path)
    except OSError:
      pass
  else:
    with open(path, 'w') as f:
      f.write('1')

