pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'covidtracking')
gnome = import('gnome')

gnome.compile_resources('covidtracking',
  'covidtracking.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'covidtracking.in',
  output: 'covidtracking',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

covidtracking_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'images/vaccine.py',
  'images/top_provinces.py',
  'images/least_provinces.py',
  'images/total_dose.py',
  'images/one_month_daily_dose.py',
  'images/three_month_daily_dose.py',
  'images/total_daily_dose.py',
  'images/total_dose.py',
  'cases/case.py',
  'cases/one_month_daily_case.py',
  'cases/three_month_daily_case.py',
  'cases/total_daily_case.py',
  'cases/one_month_daily_death.py',
  'cases/three_month_daily_death.py',
  'cases/total_daily_death.py',
  'cases/top_case_province.py',
  'cases/least_case_province.py',
  'news/news.py',
]

install_data(covidtracking_sources, install_dir: moduledir)
