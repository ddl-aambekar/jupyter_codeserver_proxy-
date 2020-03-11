"""
Return config on servers to start for codeserver

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil

def setup_codeserver():
    # Make sure codeserver is in $PATH
    def _codeserver_command(port):
        full_path = shutil.which('code-server')
        if not full_path:
            raise FileNotFoundError('Can not find code-server in $PATH')
        working_dir = os.getenv("CODE_WORKINGDIR", None)
        if working_dir is None:
            working_dir = os.getenv("JUPYTER_SERVER_ROOT", ".")

        return [full_path, working_dir, '--port=' + str(port), "--auth none", " --disable-telemetry"]
        
    return {
        'command': _codeserver_command,
        'timeout': 20,
        'launcher_entry': {
            'title': 'VS Code IDE 2021',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'icons', 'vscode.svg')
        }
    }
