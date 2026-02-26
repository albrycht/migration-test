# ***********************************************************************************************************
#
# Starfish Storage Corporation ("Starfish") CONFIDENTIAL
# Unpublished Copyright (c) 2011 - present Starfish Storage Corporation, All Rights Reserved.
#
# NOTICE: This file and its contents (1) constitute Starfish's "External Code" under Starfish's most-recent
# Limited Software End-User License Agreement, and (2) is and remains the property of Starfish. The
# intellectual and technical concepts contained herein are proprietary to Starfish and may be covered by
# U.S. and/or foreign patents or patents in process, and are protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material is strictly forbidden unless prior
# written permission is obtained from Starfish. Access to the source code contained herein is hereby
# forbidden to anyone except (A) current Starfish employees, managers, or contractors who have executed
# confidentiality or nondisclosure agreements explicitly covering such access, and (B) licensees of
# Starfish's software.
#
# ANY REPRODUCTION, COPYING, MODIFICATION, DISTRIBUTION, PUBLIC PERFORMANCE, OR PUBLIC DISPLAY OF OR
# THROUGH USE OF THIS SOURCE CODE WITHOUT THE EXPRESS WRITTEN CONSENT OF STARFISH IS STRICTLY PROHIBITED
# AND IS IN VIOLATION OF APPLICABLE LAWS AND INTERNATIONAL TREATIES. THE RECEIPT OR POSSESSION OF THIS
# FILE OR ITS CONTENTS AND/OR RELATED INFORMATION DOES NOT CONVEY OR IMPLY ANY RIGHTS TO REPRODUCE,
# DISCLOSE, OR DISTRIBUTE ITS CONTENTS, OR TO MANUFACTURE, USE, OR SELL ANYTHING THAT IT MAY DESCRIBE, IN
# WHOLE OR IN PART.
#
# FOR U.S. GOVERNMENT CUSTOMERS REGARDING THIS DOCUMENTATION/SOFTWARE
#   These notices shall be marked on any reproduction of this data, in whole or in part.
#   NOTICE: Notwithstanding any other lease or license that may pertain to, or accompany the delivery of,
#   this computer software, the rights of the Government regarding its use, reproduction and disclosure are
#   as set forth in Section 52.227-19 of the FARS Computer Software-Restricted Rights clause.
#   RESTRICTED RIGHTS NOTICE: Use, duplication, or disclosure by the Government is subject to the
#   restrictions as set forth in subparagraph (c)(1)(ii) of the Rights in Technical Data and Computer
#   Software clause at DFARS 52.227-7013.
#
# ***********************************************************************************************************
"""
Add custom_worker_options column to crawler_options table.
"""

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision = "0107"
down_revision = "0106"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("crawler_options", sa.Column("custom_worker_options", JSONB, nullable=True), schema="sf_scans")
