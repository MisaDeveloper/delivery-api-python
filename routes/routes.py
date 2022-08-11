from flask import Blueprint

from controllers.CreateController import CreateController
from controllers.UpdateController import UpdateController
from controllers.DeleteController import DeleteController
from controllers.GetOrderController import GetOrderController
from controllers.ChangeStateController import ChangeStateController

routes_bp = Blueprint('routes_bp', __name__)

routes_bp.route('/get-order/<orderId>', methods=['GET']) (GetOrderController)
routes_bp.route('/create/', methods=['POST']) (CreateController)
routes_bp.route('/update/<orderId>', methods=['PUT']) (UpdateController)
routes_bp.route('/delete/<orderId>', methods=['DELETE']) (DeleteController)
routes_bp.route('/change-state/<orderId>/<orderState>', methods=['PUT']) (ChangeStateController)