import statistics
def mode(m):
  try:
    return(statistics.mode(m))
  except statistics.StatisticsError:
    return("no mode")
