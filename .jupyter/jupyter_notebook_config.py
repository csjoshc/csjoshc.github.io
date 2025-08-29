# Project-level Jupyter configuration
# This ensures the correct Python 3.11 kernel is used

c = get_config()

# Set the default kernel to our custom kernel
c.NotebookApp.kernel_name = 'csjoshc-python311'

# Trust our custom kernel
c.NotebookApp.trust_xheaders = True

# Auto-start settings
c.NotebookApp.open_browser = False
c.NotebookApp.default_url = '/tree'

# Kernel manager configuration
c.KernelSpecManager.whitelist = ['csjoshc-python311']

# Ensure kernel discovery works
c.KernelSpecManager.kernel_spec_class = 'jupyter_client.kernelspec.KernelSpec'
