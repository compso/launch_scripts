import os


def getEnv(key, default):
    value = os.environ.get(key, default)
    return value
    if key in os.environ:
        return os.environ[key]
    else:
        return default


def remove_py(filename):

    return os.path.splitext(filename)[0]


# reset the PYTHONPATH env
os.environ['PYTHONPATH']=''

envs = {
    'peregrinel_LICENSE': "5053@china.mad.solidangle.com",
    'SW': "/software",
    'ARNOLD_VERSION': getEnv('ARNOLD_VERSION', '5.2.0.1'),
    'MAYA_VERSION': getEnv('MAYA_VERSION', '2018'),
    'MTOA_VERSION': getEnv('MTOA_VERSION', '3.1.0.1'),
    'HOUDINI_VERSION': getEnv('HOUDINI_VERSION', '16.5.496'),
    'HTOA_VERSION': getEnv('HTOA_VERSION', '3.1.1'),
    'KATANA_VERSION': getEnv('KATANA_VERSION', '3.0v1'),
    'KTOA_VERSION': getEnv('KTOA_VERSION', '2.1.1.0'),
    'YETI_VERSION': getEnv('YETI_VERSION', '2.1.15'),
    'ALSHADERS_VERSION': getEnv('ALSHADERS_VERSION', '2.0.0b2'),
    'ALSHADERS_LEGACY_VERSION': getEnv('ALSHADERS_LEGACY_VERSION', '1.0.0rc20'),
    'GOLAEM_VERSION': getEnv('GOLEAEM_VERSION', '6.3.3'),
    'WALTER_VERSION': getEnv('WALTER_VERSION', '1.0.1'),
    'RMAN_VERSION': getEnv('RMAN_VERSION', '21.6'),
    'ORNATRIX_VERSION': getEnv('ORNATRIX_VERSION', '2.1.2.15145'),
    'JSNOISE_VERSION': getEnv('JSNOISE_VERSION', '02102017'),
    'USD_VERSION': getEnv('USD_VERSION', '0.8.3'),
    'PYTHON_VERSION': getEnv('PYTHON_VERSION', '2.7.14'),
    'BBALEMBIC_VERSION': getEnv('BBALEMBIC_VERSION', '2.0.0'),
}

envs['SA_ROOT'] = '{SW}/solidangle'.format(**envs)
envs['MAYA_ROOT'] = '/usr/autodesk/maya{MAYA_VERSION}'
envs['MTOA_ROOT'] = "{SA_ROOT}/mtoa/{MTOA_VERSION}/{MAYA_VERSION}"
envs['HTOA_ROOT'] = "{SA_ROOT}/htoa/{HTOA_VERSION}/{HOUDINI_VERSION}"
envs['YETI_ROOT'] = "{SW}/yeti/{YETI_VERSION}/{MAYA_VERSION}"
envs['RMAN_ROOT'] = "/opt/pixar/RenderManForMaya-{RMAN_VERSION}-maya{MAYA_VERSION}/"
envs['ORNATRIX_ROOT'] = "{SW}/ornatrix/{ORNATRIX_VERSION}/"
envs['GOLAEM_ROOT'] = "{SW}/golaem/{GOLAEM_VERSION}/{MAYA_VERSION}"
envs['WALTER_ROOT'] = "{SW}/walter/{WALTER_VERSION}"
envs['WALTER_MAYA_ROOT'] = "{WALTER_ROOT}/maya/{MAYA_VERSION}"
envs['ALSHADERS_ROOT'] = "{SA_ROOT}/alshaders/{ALSHADERS_VERSION}"
envs['ALSHADERS_LEGACY_ROOT'] = "{SA_ROOT}/alshaders/{ALSHADERS_LEGACY_VERSION}"
envs['JSNOISE_ROOT'] = "{SA_ROOT}/jsnoise/{JSNOISE_VERSION}"

# resolve the root envs
for e, v in envs.items():
    envs[e] = v.format(**envs)
