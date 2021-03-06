from .postgresql import CathubPostgreSQL
from sys import argv, stdout


def main(dbfile, start_id=1, write_reaction=True, write_ase=True,
         write_publication=True, write_reaction_system=True,
         block_size=1000, start_block=0,
         db_user='catroot',
         db_password=None,
         ):

    stdout.write('Starting db2server\n')

    db = CathubPostgreSQL(user=db_user, password=db_password)
    stdout.write('Established SQL Server connection.\n')
    db.transfer(dbfile, start_id=start_id, write_reaction=write_reaction,
                write_ase=write_ase,
                write_publication=write_publication,
                write_reaction_system=write_reaction_system,
                block_size=block_size,
                start_block=start_block)


if __name__ == '__main__':
    dbfile = argv[1]
    main(dbfile)
