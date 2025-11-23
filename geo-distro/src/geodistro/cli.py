"""
Command-line interface for Geo Distribution
"""

import click
from geodistro.installer import GeoDistroInstaller
from geodistro.verifier import verify_installation

@click.group()
def cli():
    """Geo Distribution - One-click setup for geospatial libraries"""
    pass

@cli.command()
@click.option('--env-name', default='geo-distro', help='Environment name')
@click.option('--no-shortcuts', is_flag=True, help='Skip creating shortcuts')
@click.option('-v', '--verbose', is_flag=True, help='Verbose output')
def install(env_name, no_shortcuts, verbose):
    """Install the complete Geo Distribution"""
    installer = GeoDistroInstaller(verbose=verbose)
    installer.install_all(
        env_name=env_name,
        create_shortcuts=not no_shortcuts
    )

@cli.command()
def verify():
    """Verify the installation"""
    verify_installation()

@cli.command()
@click.option('--env-name', default='geo-distro', help='Environment name to remove')
def uninstall(env_name):
    """Uninstall Geo Distribution environment"""
    if click.confirm(f"Are you sure you want to remove the '{env_name}' environment?"):
        try:
            import subprocess
            subprocess.run(['conda', 'remove', '-n', env_name, '--all', '-y'], check=True)
            click.echo(f"✓ Environment '{env_name}' removed successfully")
        except subprocess.CalledProcessError:
            click.echo(f"✗ Failed to remove environment '{env_name}'")

@cli.command()
def info():
    """Show information about Geo Distribution"""
    click.echo("🌍 Geo Distribution")
    click.echo("=" * 50)
    click.echo("A comprehensive one-click installation package for")
    click.echo("geospatial libraries, similar to Anaconda distribution.")
    click.echo("\nIncludes:")
    click.echo("  • Core geospatial libraries (GDAL, PROJ, GEOS)")
    click.echo("  • Python geospatial tools (GeoPandas, Rasterio)")
    click.echo("  • Web mapping (Folium, ipyleaflet, Kepler.gl)")
    click.echo("  • Google Maps tools")
    click.echo("  • Advanced spatial analytics")
    click.echo("  • Jupyter Lab with geo extensions")

def main():
    cli()

if __name__ == '__main__':
    main()