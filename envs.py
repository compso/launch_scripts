import os

s = '*'*30


def getEnv(key, default):
    value = os.environ.get(key, default)
    return value
    if key in os.environ:
        return os.environ[key]
    else:
        return default


def remove_py(filename):

    return os.path.splitext(filename)[0]


def print_env(env):
    if env in os.environ.keys():
        print('{}\n{}'.format(s, env))
        print('\n'.join(envs[env].format(**envs).split(':')))


# reset the PYTHONPATH env
# os.environ['PYTHONPATH']=''

envs = {
    'peregrinel_LICENSE': "5053@localhost",
    'SW': "/software",
    'ARNOLD_VERSION': getEnv('ARNOLD_VERSION', '7.1.3.1'),
    'MAYA_VERSION': getEnv('MAYA_VERSION', '2023'),
    'MTOA_VERSION': getEnv('MTOA_VERSION', '5.2.1'),
    'BIFROST_VERSION': getEnv('BIFROST_VERSION', '2.5.0.0'),
    'MAYAUSD_VERSION': getEnv('MAYAUSD_VERSION', '0.17.0'),
    'HOUDINI_VERSION': getEnv('HOUDINI_VERSION', '18.5.499'),
    'USD_VERSION': getEnv('USD_VERSION', '20.11'),
    'HTOA_VERSION': getEnv('HTOA_VERSION', '5.6.1'),
    'KATANA_VERSION': getEnv('KATANA_VERSION', '3.0v1'),
    'KTOA_VERSION': getEnv('KTOA_VERSION', '2.2.1.2'),
    'YETI_VERSION': getEnv('YETI_VERSION', '4.1.4'),
    'ALSHADERS_VERSION': getEnv('ALSHADERS_VERSION', '2.0.0b2'),
    'ALSHADERS_LEGACY_VERSION': getEnv('ALSHADERS_LEGACY_VERSION', '1.0.0rc21'),
    'GOLAEM_VERSION': getEnv('GOLEAEM_VERSION', '6.4'),
    'WALTER_VERSION': getEnv('WALTER_VERSION', '1.0.1'),
    'RMAN_VERSION': getEnv('RMAN_VERSION', '24.3'),
    'ORNATRIX_VERSION': getEnv('ORNATRIX_VERSION', '2.1.2.15145'),
    'JSNOISE_VERSION': getEnv('JSNOISE_VERSION', '02102017'),
    'PYTHON_VERSION': getEnv('PYTHON_VERSION', '2.7.14'),
    'BBALEMBIC_VERSION': getEnv('BBALEMBIC_VERSION', '2.0.0'),
    'IRAY_VERSION': getEnv('IRAY_VERSION', '2.1'),
    'VRAY_VERSION': getEnv('VRAY_VERSION', '5.2.1')
}

envs['SA_ROOT'] = '{SW}/solidangle'.format(**envs)
envs['MAYA_ROOT'] = '{SW}/maya/{MAYA_VERSION}'
envs['ARNOLD_ROOT'] = "{SA_ROOT}/arnold/{ARNOLD_VERSION}/"
envs['MTOA_ROOT'] = "{SA_ROOT}/mtoa/{MTOA_VERSION}/{MAYA_VERSION}"
envs['MAYA_USD_ROOT'] = "{SW}/mayausd/{MAYA_VERSION}/{MAYAUSD_VERSION}/"
envs['BIFROST_ROOT'] = "{SW}/bifrost/maya{MAYA_VERSION}/{BIFROST_VERSION}"
envs['HTOA_ROOT'] = "{SA_ROOT}/htoa/{HTOA_VERSION}/{HOUDINI_VERSION}"
envs['YETI_ROOT'] = "{SW}/yeti/{YETI_VERSION}/{MAYA_VERSION}"
envs['USD_ROOT'] = "{SW}/usd/{USD_VERSION}"
envs['RMAN_ROOT'] = "/opt/pixar/RenderManForMaya-{RMAN_VERSION}/"
envs['ORNATRIX_ROOT'] = "{SW}/ornatrix/{ORNATRIX_VERSION}/"
envs['GOLAEM_ROOT'] = "{SW}/golaem/{GOLAEM_VERSION}/{MAYA_VERSION}"
envs['WALTER_ROOT'] = "{SW}/walter/{WALTER_VERSION}"
envs['WALTER_MAYA_ROOT'] = "{WALTER_ROOT}/maya/{MAYA_VERSION}"
envs['ALSHADERS_ROOT'] = "{SA_ROOT}/alshaders/{ALSHADERS_VERSION}"
envs['ALSHADERS_LEGACY_ROOT'] = "{SA_ROOT}/alshaders/{ALSHADERS_LEGACY_VERSION}"
envs['JSNOISE_ROOT'] = "{SA_ROOT}/jsnoise/{JSNOISE_VERSION}"
envs['IRAY_ROOT'] = "{SW}/iray/{IRAY_VERSION}/{MAYA_VERSION}"
envs['VRAY_ROOT'] = "{SW}/vray/{VRAY_VERSION}/{MAYA_VERSION}"

# resolve the root envs
for e, v in envs.items():
    envs[e] = v.format(**envs)
