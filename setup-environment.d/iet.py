def __after_init_iet_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']
    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                     'meta-fsl-arm',
                     'meta-openembedded/meta-oe',
                     'meta-openembedded/meta-ruby',
                     'meta-openembedded/meta-networking',
                     'meta-openembedded/meta-python',
                     'meta-reach',
                     'meta-iet',
                     'meta-qt5'
                    ]])

    # FSL EULA
    eulas.accept['meta-fsl-arm/EULA'] = 'ACCEPT_FSL_EULA = "1"'

run_after_init(__after_init_iet_yocto)
